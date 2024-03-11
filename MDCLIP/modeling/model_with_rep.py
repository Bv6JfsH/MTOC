"""
Main MDCLIP modeling function based on FLAIR
"""
import json
from PIL import Image
import pandas as pd
import torchvision
import numpy as np
from sklearn.metrics import average_precision_score, roc_auc_score

#from multi_modal_mil import MultiModalMIL
from unireplknet import *
import random
from .dictionary import definitions,description1,description_focus,description_performance
from . import constants
from .misc import wget_gdrive_secure
from timm import create_model
from torch.cuda.amp import autocast
from tqdm import tqdm
from pathlib import Path
from transformers import AutoModel, AutoTokenizer, logging
import albumentations as A
from albumentations.pytorch import ToTensorV2
import os

logging.set_verbosity_error()
os.environ["TOKENIZERS_PARALLELISM"] = "false"
# Device for training/inference
device = 'cuda' if torch.cuda.is_available() else 'cpu'
transform_list_test = []
transform_list_test.append(A.Resize(height=512, width=512))
transform_list_test.append(A.Normalize(mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5)))
transform_list_test.append(ToTensorV2())
transforms_test = A.Compose(transform_list_test)


class MDCLIP_with_rep(torch.nn.Module):
    def __init__(self, vision_type='resnet_v2', bert_type='emilyalsentzer/Bio_ClinicalBERT', vision_pretrained=True,
                 proj_dim=512, proj_bias=False, logit_scale_init_value=0.07, from_checkpoint=True, weights_path=None,
                 out_path=None, image_size=512, caption="A fundus photograph of [CLS]", projection=True,
                 norm_features=True, rep_weight=None):
        super().__init__()
        self.show_prompts = True
        self.show_loss_prompts = True
        self.show_train_prompts = True
        # Set attributes
        self.vision_type = vision_type
        self.bert_type = bert_type
        self.vision_pretrained = vision_pretrained
        self.proj_dim = proj_dim
        self.proj_bias = proj_bias
        self.logit_scale_init_value = logit_scale_init_value
        self.from_checkpoint = from_checkpoint
        self.weights_path = weights_path
        self.out_path = out_path
        self.image_size = image_size
        self.caption = caption
        # Use of projection head and feature normalization on vision encoder
        # (only relevant during transferability stage)
        self.projection = projection
        self.norm_features = norm_features
        self.linear = torch.nn.Linear(512, 7)
        # Set vision and text encoder

        if(self.vision_type == 'resnet_v2' or 'resnet_v1' or 'resnext' or 'densenet'):
            self.vision_model = VisionModel(vision_type=self.vision_type, pretrained=self.vision_pretrained,
                                            proj_dim=self.proj_dim, proj_bias=self.proj_bias, projection=self.projection,
                                            norm=self.norm_features)
        if(self.vision_type == 'replknet'):
            self.vision_model = create_model('unireplknet_p', num_classes=None, in_22k_pretrained=True,
                                      weight=rep_weight)
            self.vision_model.output_mode = 'features'


        self.vision_model.to(device)

        self.text_model = TextModel(bert_type=self.bert_type, proj_dim=self.proj_dim, proj_bias=self.proj_bias,
                                    projection=self.projection, norm=self.norm_features)

        # learnable temperature for contrastive loss
        self.logit_scale = torch.nn.Parameter(torch.log(torch.tensor(1 / self.logit_scale_init_value)))

        # Load pretrained weights
        if from_checkpoint:
            self.load_from_pretrained(self.weights_path)

        # Set model to device
        self.to(device)

    def load_from_pretrained(self, weights_path=None):

        if weights_path is None:
            import zipfile

            input_dir = constants.PATH_PRETRAINED_WEIGHTS
            pretrained_id = constants.ID_FLAIR_RESNET_V1
            pretrained_url_id = constants.URL_ID_FLAIR_RESNET_V1
            weights_path = input_dir + pretrained_id

            if not os.path.exists(input_dir + pretrained_id):
                if not os.path.exists(input_dir):
                    Path(input_dir).mkdir(parents=True, exist_ok=True)

                # download url link
                wget_gdrive_secure(pretrained_url_id, input_dir, filename="weights.zip")

                # unzip
                zipf = zipfile.ZipFile(input_dir + "weights.zip")
                zipf.extractall(input_dir)
                zipf.close()
                print('\n Download model to:', input_dir + pretrained_id)

        state_dict = torch.load(weights_path, map_location='cpu')
        self.load_state_dict(state_dict, strict=False)
        print('load model weight from:', weights_path)


    def softce_clip_loss(self, logits_per_text, target_pseudo):
        caption_loss = self.ce_loss(logits_per_text, target_pseudo.T)
        image_loss = self.ce_loss(logits_per_text.T, target_pseudo)
        return (caption_loss + image_loss) / 2.0


    def ce_loss(self, pred_logit, ref):
        ce_loss = torch.nn.functional.cross_entropy(pred_logit, ref)
        return ce_loss

    def compute_logits(self, img_emb, text_emb):

        self.logit_scale.data = torch.clamp(self.logit_scale.data, 0, 4.6052)
        # logit_scale = e^(logit_scale)
        logit_scale = self.logit_scale.exp()

        logits_per_text = torch.matmul(text_emb, img_emb.t()) * logit_scale
        #
        return logits_per_text.t()


    def fit(self, datalaoders, epochs=30, lr=5e-4, weight_decay=1e-5, scheduler=True, warmup_epoch=1, store_num=5,
            transforms=None, record_name=None):
        best_map = 0
        print(record_name)

        optimizer = torch.optim.AdamW(self.parameters(), lr=lr, weight_decay=weight_decay)
        record = record_name+'_log.txt'
        print(record)
        file_test = record_name+'_test_ap.txt'
        file_val = record_name+'_val_ap.txt'
        file_train = record_name + '_train_ap.txt'
        file_val_aoc = record_name + '_val_aoc.txt'
        file_test_aoc = record_name + '_test_aoc.txt'


        if scheduler:
            from MDCLIP.pretraining.utils import get_scheduler_per_iteration
            scheduler = get_scheduler_per_iteration(optimizer, lr, warmup_epoch, len(datalaoders["train"]))
        else:
            scheduler = None

        # Training along epochsf
        epoch = 1
        while epoch <= epochs:

            # Train epoch


            loss_epoch, scheduler_lr, adamW_lr, adamW_weight_decay = self.train_epoch_with_text_weights_3_layers(datalaoders["train"], optimizer,
                                                                                       scheduler, transforms, epoch,label_weight=100,focus_weight=0,perfor_weight=10,isdown=False)



            val_mAP, test_mAP, train_mAP, val_AP_list, test_AP_list, train_AP_list,val_macro_auroc,test_macro_auroc = self.evaluate_val_and_test_and_train(datalaoders["train_eval"], datalaoders["val"],datalaoders["test"], file_val, file_test, file_train,file_val_aoc,file_test_aoc, class_num=7)


            print(self.logit_scale.data)
            # loss_epoch = self.train_epoch_with_average_text(datalaoders["train"], optimizer, scheduler, transforms, epoch)
            # Display epoch-wise loss
            log = 'Epoch=%d: ave_loss=%2.5f,val_macro_auroc=%2.5f,test_macro_auroc=%2.5f,val_ap_list=%s,val_mAP=%2.5f,test_ap_list=%s,test_mAP=%2.5f,train_ap_list=%s,train_mAP=%2.5f, sch_lr=%s, adamW_lr=%f, adamW_weight_decay=%f' % (epoch, loss_epoch,val_macro_auroc,test_macro_auroc,val_AP_list,val_mAP,test_AP_list,test_mAP,train_AP_list,train_mAP, scheduler_lr, adamW_lr, adamW_weight_decay)
            print(log)
            # log = ('{}'.format(val_loss))
            with open(record, 'a') as f:
                f.write(log+'\n')

            if(epoch==1):
                best_map = val_mAP
            else:
                if(val_mAP > best_map and epoch>=80 and epoch<=120):
                    best_map = val_mAP
                    torch.save(self.state_dict(),
                           self.out_path + self.vision_type + record_name+'bestmAP' + '.pth')

            # Save model
            if epoch % store_num == 0:
                if self.out_path is not None:
                    if not os.path.isdir(self.out_path):
                        os.mkdir(self.out_path)
                    torch.save(self.state_dict(),
                               self.out_path + self.vision_type + '_epoch' + str(epoch) + record_name + '.pth')

            # Update epoch
            epoch += 1

        self.predict_the_best_mAP(self.out_path + self.vision_type + record_name+'bestmAP' + '.pth', datalaoders["test"], file_test, file_test_aoc, class_num=7)





    def predict_the_best_mAP(self,path,loader_test,file_test,file_test_aoc,class_num = 46):
        text = ["normal", "epiretinal membrane",
                 "macular edema", "diabetic retinopathy",
                 "non-exudative age related macular degeneration",
                 "exudative age related macular degeneration",
                 "degenerative myopia"]
        epoch_test_iterator = tqdm(
            loader_test, desc="Test Prediction (X / X Steps) (mAP=X.X)", dynamic_ncols=True
        )
        test_model = MDCLIP_with_rep(vision_type='replknet', out_path="./local_data/results/pretraining/", from_checkpoint=True,
                                     vision_pretrained=True, weights_path=path)
        test_model.eval()
        with torch.no_grad():
            with autocast():
                refs, preds = [], []
                re = []
                true_label_list = []
                text_input_ids, text_attention_mask = test_model.preprocess_text(text)
                text_embeds = test_model.text_model(text_input_ids, text_attention_mask)
                for step, batch in enumerate(epoch_test_iterator):
                    images = batch["image"].to(device).to(torch.float32)
                    Y = batch["labels"]
                    true_label = torch.stack(Y, dim=1)
                    true_label_list.append(true_label)
                    img_embeds = test_model.vision_model(images)
                    logits = test_model.compute_logits(img_embeds, text_embeds)
                    re.append(logits)
                true_label_tensor = torch.cat(true_label_list, dim=0).cpu().numpy()
                predicted_score = torch.cat(re, dim=0).cpu().numpy()
                AP_list_test = []
                auroc_list_test = []
                with open(file_test, 'a') as f:
                    for j in range(class_num):
                        true_label_j = true_label_tensor[:, j]
                        predicted_score_j = predicted_score[:, j]
                        AP_1 = "null"
                        if (np.any(true_label_j != 0)):
                            AP_1 = average_precision_score(true_label_j, predicted_score_j)
                            auroc_1 = roc_auc_score(true_label_j, predicted_score_j)
                            AP_list_test.append(AP_1)
                            auroc_list_test.append(auroc_1)
                        f.write(str(AP_1) + ',')
                    test_mAP = sum(AP_list_test) / len(AP_list_test)
                    test_macro_auroc = sum(auroc_list_test) / len(auroc_list_test)
                    f.write(str(sum(AP_list_test) / len(AP_list_test)) + '\n')

                AP_list_test = []
                auroc_list_test = []
                with open(file_test_aoc, 'a') as f:
                    for j in range(class_num):
                        true_label_j = true_label_tensor[:, j]
                        predicted_score_j = predicted_score[:, j]
                        auroc_1 = "null"
                        if (np.any(true_label_j != 0)):
                            AP_1 = average_precision_score(true_label_j, predicted_score_j)
                            auroc_1 = roc_auc_score(true_label_j, predicted_score_j)
                            AP_list_test.append(AP_1)
                            auroc_list_test.append(auroc_1)

                        f.write(str(auroc_1) + ',')
                    test_mAP = sum(AP_list_test) / len(AP_list_test)
                    test_macro_auroc = sum(auroc_list_test) / len(auroc_list_test)
                    f.write(str(sum(auroc_list_test) / len(auroc_list_test)) + '\n')




    def evaluate_val_and_test_and_train(self, loader_train, loader_val, loader_test, file_val, file_test, file_train,file_val_aoc,file_test_aoc, class_num = 46):
        self.eval()
        loss_ave = 0
        val_mAP = 0
        test_mAP = 0
        epoch_val_iterator = tqdm(
            loader_val, desc="Val Prediction (X / X Steps) (mAP=X.X)", dynamic_ncols=True
        )
        text = ["normal", "epiretinal membrane",
                 "macular edema", "diabetic retinopathy",
                 "non-exudative age related macular degeneration",
                 "exudative age related macular degeneration",
                 "degenerative myopia"]


        # text = ['normal','diabetic retinopathy', 'age-related macular degeneration',
        #                   'media haze', 'drusens', 'myopia', 'branch retinal vein occlusion',
        #                   'tessellation','epiretinal membrane',  'laser scar',
        #                  'macular scar',  'central serous retinopathy', 'optic disc cupping',
        #                  'central retinal vein occlusion', 'tortuous vessels', 'asteroid hyalosis',
        #                  'optic disc pallor',  'optic disc edema', 'shunt',
        #                 'anterior ischemic optic neuropathy',  'parafoveal telangiectasia',
        #                  'retinal traction', 'retinitis',  'chorioretinitis',  'edudates',
        #                 'retinal pigment epithelium changes',  'macular hole',
        #                 'retinitis pigmentosa',  'cotton wool spots',  'colobomas',
        #                  'optic disc pit maculopathy',  'preretinal haemorrhage',
        #                  'myelinated nerve fibers',  'haemorrhagic retinopathy',
        #                  'central retinal artery occlusion',  'tilted disc',
        #                   'cystoid macular edema',  'post traumatic choroidal rupture',
        #                  'choroidal folds', 'vitreous haemorrhage',  'macroaneurysm',
        #                  'vasculitis', 'branch retinal artery occlusion',  'plaque',
        #                  'haemorrhagic pigment epithelial detachment', 'collaterals']

        # text = ['a disease', 'diabetic retinopathy', 'age-related macular degeneration',
        #         'media haze', 'drusens', 'myopia', 'branch retinal vein occlusion',
        #         'tessellation', 'epiretinal membrane', 'laser scar',
        #         'macular scar', 'central serous retinopathy', 'optic disc cupping',
        #         'central retinal vein occlusion', 'tortuous vessels', 'asteroid hyalosis',
        #         'optic disc pallor', 'optic disc edema', 'optociliary shunt vessels',
        #         'anterior ischemic optic neuropathy', 'parafoveal telangiectasia',
        #         'retinal traction', 'retinitis', 'chorioretinitis', 'exudation',
        #         'retinal pigment epithelium changes', 'macular hole',
        #         'retinitis pigmentosa', 'other']


        # text = ['normal',
        #         'diabetic retinopathy',
        #         'glaucoma',
        #         'cataract',
        #         'age-related macular degeneration',
        #         'hypertensive retinopathy',
        #         'myopia',
        #         'other disease']

        
        with torch.no_grad():
            with autocast():
                refs, preds = [], []
                re = []
                true_label_list = []
                text_input_ids, text_attention_mask = self.preprocess_text(text)
                text_embeds = self.text_model(text_input_ids, text_attention_mask)
                for step, batch in enumerate(epoch_val_iterator):
                    images = batch["image"].to(device).to(torch.float32)
                    Y = batch["labels"]
                    true_label = torch.stack(Y,dim=1)
                    true_label_list.append(true_label)
                    img_embeds = self.vision_model(images)
                    logits = self.compute_logits(img_embeds, text_embeds)
                    re.append(logits)
                true_label_tensor = torch.cat(true_label_list,dim=0).cpu().numpy()
                predicted_score =torch.cat(re,dim=0).cpu().numpy()
                AP_list_val = []
                auroc_list_val = []
                with open(file_val, 'a') as f:
                    for j in range(class_num):
                        true_label_j = true_label_tensor[:, j]
                        predicted_score_j = predicted_score[:, j]
                        AP_1 = "null"
                        
                        if(np.any(true_label_j != 0)):

                            AP_1 = average_precision_score(true_label_j, predicted_score_j)
                            auroc_1 = roc_auc_score(true_label_j, predicted_score_j)
                            AP_list_val.append(AP_1)
                            auroc_list_val.append(auroc_1)

                        f.write(str(AP_1) + ',')
                        
                        
                    val_mAP = sum(AP_list_val) / len(AP_list_val)
                    val_macro_auroc = sum(auroc_list_val) / len(auroc_list_val)
                    f.write(str(sum(AP_list_val) / len(AP_list_val)) + '\n')
                    

                AP_list_val = []
                auroc_list_val = []
                with open(file_val_aoc, 'a') as f:
                    for j in range(class_num):
                        true_label_j = true_label_tensor[:, j]
                        predicted_score_j = predicted_score[:, j]
                        auroc_1 = "null"

                        if (np.any(true_label_j != 0)):
                            AP_1 = average_precision_score(true_label_j, predicted_score_j)
                            auroc_1 = roc_auc_score(true_label_j, predicted_score_j)
                            AP_list_val.append(AP_1)
                            auroc_list_val.append(auroc_1)
                        f.write(str(auroc_1) + ',')

                    val_mAP = sum(AP_list_val) / len(AP_list_val)
                    val_macro_auroc = sum(auroc_list_val) / len(auroc_list_val)
                    
                    f.write(str(sum(auroc_list_val) / len(auroc_list_val)) + '\n')
                




        # epoch_train_iterator = tqdm(
        #     loader_train, desc="Train Prediction (X / X Steps) (mAP=X.X)", dynamic_ncols=True
        # )
        #
        # with torch.no_grad():
        #     with autocast():
        #         refs, preds = [], []
        #         re = []
        #         true_label_list = []
        #         text_input_ids, text_attention_mask = self.preprocess_text(text)
        #         text_embeds = self.text_model(text_input_ids, text_attention_mask)
        #         for step, batch in enumerate(epoch_train_iterator):
        #             images = batch["image"].to(device).to(torch.float32)
        #             Y = batch["labels"]
        #             true_label = torch.stack(Y,dim=1)
        #             true_label_list.append(true_label)
        #             img_embeds = self.vision_model(images)
        #             logits = self.compute_logits(img_embeds, text_embeds)
        #             re.append(logits)
        #         true_label_tensor = torch.cat(true_label_list,dim=0).cpu().numpy()
        #         predicted_score =torch.cat(re,dim=0).cpu().numpy()
        #         AP_list_train = []
        #         with open(file_train, 'a') as f:
        #             for j in range(class_num):
        #                 true_label_j = true_label_tensor[:, j]
        #                 predicted_score_j = predicted_score[:, j]
        #                 AP_1 = average_precision_score(true_label_j, predicted_score_j)
        #                 AP_list_train.append(AP_1)
        #                 f.write(str(AP_1) + ',')
        #             train_mAP = sum(AP_list_train) / len(AP_list_train)
        #             f.write(str(sum(AP_list_train) / len(AP_list_train)) + '\n')

        train_mAP = 0
        AP_list_train = []
        train_mAP = 0
        AP_list_test = []
        test_macro_auroc = []


        return val_mAP ,test_mAP,train_mAP, AP_list_val, AP_list_test,AP_list_train,val_macro_auroc,test_macro_auroc









    def train_epoch_with_text_weights_3_layers(self, loader, optimizer, scheduler=None, transforms=None, epoch=1, label_weight = 100.0,focus_weight=20.0,perfor_weight=10.0,isdown =False):
        self.train()
        max_grad_norm, scaler = 1, torch.cuda.amp.GradScaler()
        loss_ave = 0.0

        # Set iterator
        epoch_iterator = tqdm(
            loader, desc="Training (X / X Steps) (loss=X.X)", dynamic_ncols=True
        )

        # Iterate trough training batches
        for step, batch in enumerate(epoch_iterator):
            # Retrieve documents,images = [8,3,512,512]
            images = batch["image"].to(device).to(torch.float32)
            # Create text tokens,input_ids = [8,10],attention_mask = [8,10]
            if(self.show_train_prompts == True):
                self.show_train_prompts =False
                temp = list(batch["report"][0])
                print(f"now prompts are:{temp}")

            # text_tokens = self.text_model.tokenize(list(batch["report"][0]))
            text_tokens_labels = self.text_model.tokenize(list(batch["report"][0]))

            prompts = [description_focus[i] for i in batch["sel_category"]]
            prompts_perfor = [description_performance[i] for i in batch["sel_category"]]
            new_prompts = [random.sample(i, 1)[0] for i in prompts]
            new_prompts_perfor = [random.sample(i, 1)[0] for i in prompts_perfor]
            new_cat = ["A fundus photograph of [CLS]".replace("[CLS]",i) for i in new_prompts]
            new_cat_perfor = ["A fundus photograph of [CLS]".replace("[CLS]", i) for i in new_prompts_perfor]
            text_tokens_prompts = self.text_model.tokenize(new_cat)
            text_tokens_prompts_perfor = self.text_model.tokenize(new_cat_perfor)

            input_ids_labels = text_tokens_labels["input_ids"].to(device).to(torch.long)
            attention_mask_labels = text_tokens_labels["attention_mask"].to(device).to(torch.long)

            input_ids_prompts_perfor = text_tokens_prompts_perfor["input_ids"].to(device).to(torch.long)
            attention_mask_prompts_perfor = text_tokens_prompts_perfor["attention_mask"].to(device).to(torch.long)


            input_ids_prompts = text_tokens_prompts["input_ids"].to(device).to(torch.long)
            attention_mask_prompts = text_tokens_prompts["attention_mask"].to(device).to(torch.long)





            # all_cat = [eval(cat) for cat in batch['all_categories']]
            # co = [[each_cat in each_all_cat for each_cat in batch["sel_category"]] for each_all_cat in all_cat]

            # coocurrence = np.array(
            #     [[iDesc == iiDesc for iDesc in batch["sel_category"]] for iiDesc in batch["sel_category"]], np.float32)

            coocurrence = np.array([[each_cat in each_all_cat for each_cat in batch["sel_category"]] for each_all_cat in
                                    [eval(cat) for cat in batch['all_categories']]], np.float32)

            # target = torch.tensor(coocurrence / coocurrence.sum(-1)).to(device).to(torch.float32)
            target = torch.tensor(coocurrence).to(device).to(torch.float32)
            # Forward
            with autocast():

                # Image augmentation
                if transforms is not None:
                    images = transforms(images)

                # Forward vision and text encoder,images = [8,3,512,512],img_embeds = [8,512], text_embeds = [8,512]
                img_embeds = self.vision_model(images)
                text_embeds_labels = self.text_model(input_ids_labels, attention_mask_labels)
                text_embeds_prompts = self.text_model(input_ids_prompts, attention_mask_prompts)
                text_embeds_prompts_perfor = self.text_model(input_ids_prompts_perfor, attention_mask_prompts_perfor)

                # text_embeds = text_embeds_labels
                y = (focus_weight / 100.0)
                z = (perfor_weight / 100.0)
                if(isdown == True):
                    y = (focus_weight / 100.0) * np.exp(-0.05 * epoch)
                    z = (perfor_weight / 100.0) * np.exp(-0.05 * epoch)

                text_embeds = text_embeds_labels * (label_weight / 100.0) + text_embeds_prompts * y + text_embeds_prompts_perfor * z

                #text_embeds = text_embeds*(100.0/(label_weight+y+z))

                # text_embeds = text_embeds_labels*(label_weight/100.0) + text_embeds_prompts * (focus_weight/100.0) +text_embeds_prompts_perfor*(perfor_weight/100.0)
                # Compute similarity matrix and logits
                logits_per_image = self.compute_logits(img_embeds, text_embeds)
                logits_per_text = logits_per_image.t()

                # Compute cross-entropy loss
                loss = self.softce_clip_loss(logits_per_text, target)

            # Update model with scaler
            scaler.scale(loss).backward()

            scaler.unscale_(optimizer)

            torch.nn.utils.clip_grad_norm_(self.parameters(), max_grad_norm)

            scaler.step(optimizer)

            scaler.update()

            optimizer.zero_grad()

            # Overall losses track

            loss_ave += loss.item()

            torch.cuda.empty_cache()

            # Set description

            epoch_iterator.set_description(
                "Epoch=%d: Training (%d / %d Steps) " % (epoch, step + 1, len(loader)) +
                "- loss_value: " + str(round(loss.item(), 3))
            )

            # Update optimizer scheduler
            if scheduler is not None:
                scheduler.step()

        adamW_lr = 0
        adamW_weight_decay = 0

        for param_group in optimizer.param_groups:
            adamW_lr = param_group['lr']
            adamW_weight_decay = param_group['weight_decay']

        self.eval()
        return loss_ave / len(loader), scheduler.get_last_lr(),adamW_lr,adamW_weight_decay


    def forward(self, image, text):

        self.eval()

        # Pre-process image
        image = self.preprocess_image(image)

        # Pre-process text

        text_input_ids, text_attention_mask = self.preprocess_text(text)

        # Forward vision and text encoder
        with torch.no_grad():
            img_embeds = self.vision_model(image)
            text_embeds = self.text_model(text_input_ids, text_attention_mask)

            # Compute similarity matrix and logits
            logits = self.compute_logits(img_embeds, text_embeds)

            # Compute probabilities
            probs = logits.softmax(dim=-1)

        return probs.cpu().numpy(), logits.cpu().numpy()




    def forward2(self, image, text):
        self.eval()

        # Pre-process image
        image = self.preprocess_image(image)

        # Pre-process text

        text_input_ids, text_attention_mask = self.preprocess_text(text)

        # Forward vision and text encoder
        with torch.no_grad():
            img_embeds = self.vision_model(image)
            text_embeds = self.text_model(text_input_ids, text_attention_mask)

            # Compute similarity matrix and logits
            logits = self.compute_logits(img_embeds, text_embeds)

        return logits.cpu().numpy()



    def forward3(self, image, text):

        self.eval()

        # Pre-process image
        image = self.preprocess_image(image)

        # Pre-process text

        text_input_ids_labels, text_attention_mask_labels = self.preprocess_text(text)

        # prompts = [description1[i] for i in text]
        # new_cat = ["A fundus photograph of [CLS]".replace("[CLS]", i) for i in prompts]

        """
                for iKey in range(len(categories)):

            # Replace text prompt with expert knowledge descriptions
            if domain_knowledge and categories[iKey] in list(definitions.keys()):
                descriptions = definitions[categories[iKey]]
                if categories[iKey] not in descriptions:
                    descriptions.append(categories[iKey])
            else:
                descriptions = [categories[iKey]]

            # Forwards prompts trough text encoder
            with torch.no_grad():
                print(descriptions)
                descriptions = [self.caption.replace("[CLS]", iDescription) for iDescription in descriptions]
                text_token = self.text_model.tokenizer(descriptions, truncation=True, padding=True, return_tensors='pt')
                input_ids = text_token["input_ids"].to(device).to(torch.long)
                attention_mask = text_token["attention_mask"].to(device).to(torch.long)

                text_embeds = self.text_model(input_ids, attention_mask)

            text_embeds_dict[categories[iKey]] = text_embeds.mean(0).unsqueeze(0)

        text_embeds_dict = text_embeds_dict
        text_embeds = torch.concat(list(text_embeds_dict.values()))
        """

        text_embeds_dict = {}
        for iKey in range(len(text)):
            descriptions = description1[text[iKey]]
            with torch.no_grad():
                descriptions = [self.caption.replace("[CLS]", iDescription) for iDescription in descriptions]
                text_token = self.text_model.tokenizer(descriptions, truncation=True, padding=True, return_tensors='pt')
                input_ids = text_token["input_ids"].to(device).to(torch.long)
                attention_mask = text_token["attention_mask"].to(device).to(torch.long)
                text_embeds = self.text_model(input_ids, attention_mask)
            text_embeds_dict[text[iKey]] = text_embeds.mean(0).unsqueeze(0)
        text_embeds_dict = text_embeds_dict
        text_embeds_prompts_sum = torch.concat(list(text_embeds_dict.values()))


        # text_tokens = self.text_model.tokenize(new_cat)
        # input_ids_prompts = text_tokens["input_ids"].to(device).to(torch.long)
        # attention_mask_prompts = text_tokens["attention_mask"].to(device).to(torch.long)


        # Forward vision and text encoder
        with torch.no_grad():
            img_embeds = self.vision_model(image)
            text_embeds_labels = self.text_model(text_input_ids_labels, text_attention_mask_labels)
            # text_embeds_prompts = self.text_model(input_ids_prompts, attention_mask_prompts)
            # text_embeds_prompts_sum = torch.mean(text_embeds_prompts,dim=0)
            text_embeds = text_embeds_labels + 0.2*text_embeds_prompts_sum

            # Compute similarity matrix and logits
            logits = self.compute_logits(img_embeds, text_embeds)

        return logits.cpu().numpy()

    def predict_by_text_embeds_and_image(self, image, text_embeds):
        self.eval()
        image = self.preprocess_image(image)
        with torch.no_grad():
            img_embeds = self.vision_model(image)

            # Compute similarity matrix and logits
            logits = self.compute_logits(img_embeds, text_embeds)
        return logits.cpu().numpy()

    def preprocess_image(self, image):

        # Set image dtype
        if image.dtype != np.float32:
            image = np.float32(image)

        # Intensity scaling
        if image.max() > 0:
            image /= 255

        # Channel first
        if len(image.shape) > 2:
            image = np.transpose(image, (2, 0, 1))
        else:
            image = np.expand_dims(image, 0)

        # Batch dimension
        image = np.expand_dims(image, 0)

        # Resize to training size using a canvas
        image = torch.tensor(image)
        sizes = image.shape[-2:]
        max_size = max(sizes)
        scale = max_size / self.image_size
        image = torchvision.transforms.Resize((int(image.shape[-2] / scale), int((image.shape[-1] / scale))))(image)
        image = torch.nn.functional.pad(image, (
        0, self.image_size - image.shape[-1], 0, self.image_size - image.shape[-2], 0, 0))

        # Set format and device
        image = image.to(torch.float32).to(device)
        return image



    def preprocess_loss_text(self, text):

        # Create text prompt
        prompts = [self.caption.replace("[CLS]", category) for category in text]
        if(self.show_loss_prompts==True):
            self.show_loss_prompts = False
            print(f"noew prompts are:{prompts}")
        # Create text tokens
        text_tokens = self.text_model.tokenize(prompts)
        input_ids = text_tokens["input_ids"].to(device).to(torch.long)
        attention_mask = text_tokens["attention_mask"].to(device).to(torch.long)

        return input_ids, attention_mask



    def preprocess_text(self, text):

        # Create text prompt
        prompts = [self.caption.replace("[CLS]", category) for category in text]
        if(self.show_prompts==True):
            self.show_prompts = False
            print(f"now prompts are:{prompts}")
        # Create text tokens
        text_tokens = self.text_model.tokenize(prompts)
        input_ids = text_tokens["input_ids"].to(device).to(torch.long)
        attention_mask = text_tokens["attention_mask"].to(device).to(torch.long)

        return input_ids, attention_mask

    def compute_text_embeddings(self, categories, domain_knowledge=False):
        # Obtain text embeddings per class
        text_embeds_dict = {}
        for iKey in range(len(categories)):

            # Replace text prompt with expert knowledge descriptions
            if domain_knowledge and categories[iKey] in list(definitions.keys()):
                descriptions = definitions[categories[iKey]]
                if categories[iKey] not in descriptions:
                    descriptions.append(categories[iKey])
            else:
                descriptions = [categories[iKey]]

            # Forwards prompts trough text encoder
            with torch.no_grad():
                print(descriptions)
                descriptions = [self.caption.replace("[CLS]", iDescription) for iDescription in descriptions]
                text_token = self.text_model.tokenizer(descriptions, truncation=True, padding=True, return_tensors='pt')
                input_ids = text_token["input_ids"].to(device).to(torch.long)
                attention_mask = text_token["attention_mask"].to(device).to(torch.long)

                text_embeds = self.text_model(input_ids, attention_mask)

            text_embeds_dict[categories[iKey]] = text_embeds.mean(0).unsqueeze(0)

        text_embeds_dict = text_embeds_dict
        text_embeds = torch.concat(list(text_embeds_dict.values()))

        return text_embeds_dict, text_embeds


class VisionModel(torch.nn.Module):
    def __init__(self, vision_type='resnet_v1', pretrained=True, proj_dim=512, proj_bias=False, projection=True,
                 norm=True):
        super().__init__()
        self.proj_dim = proj_dim

        # Assert vision encoders
        if vision_type not in ['resnet_v1', 'resnet_v2', 'efficientnet']:
            print("Vision model should be one of resnet/efficientnet... using resnet.")
            vision_type = "resnet_v1"

        # Set vision encoder architecture and pretrained weights
        if vision_type == "resnet_v1" or vision_type == "resnet_v2":
            # Set pretrained weights from Imagenet and get model
            if vision_type == "resnet_v1":
                weights = 'IMAGENET1K_V1' if pretrained else None
            elif vision_type == "resnet_v2":
                weights = 'IMAGENET1K_V2' if pretrained else None
            else:
                weights = 'IMAGENET1K_V1' if pretrained else None
            print("Pretrained weights: " + str(weights))


            # Set number of extracted features
            self.vision_dim = 512
            self.model.fc = torch.nn.Identity()
            # Replace classifier by Identity layer
            # self.model.fc = torch.nn.Identity()
            # self.model.classifier = torch.nn.Identity()
            # self.model.fc = torch.nn.Identity()
        elif vision_type == "efficientnet":
            weights = 'IMAGENET1K_V1' if pretrained else None
            self.model = torchvision.models.efficientnet_b7(weights=weights)

            self.model.classifier = torch.nn.Identity()
            self.vision_dim = 2096
        elif vision_type == "resnext":
            weights = 'IMAGENET1K_V2' if pretrained else None
            self.model = torchvision.models.resnext101_32x8d(weights=weights)
            self.model.classifier = torch.nn.Identity()
            self.vision_dim = 2048
        elif vision_type == "densenet":
            weights = 'IMAGENET1K_V2' if pretrained else None
            self.model = torchvision.models.densenet121(weights=weights)
            self.model.classifier = torch.nn.Identity()
            self.vision_dim = 2048

        # Set output dimension
        #
        if projection:
            self.out_dim = self.proj_dim
        else:
            self.out_dim = self.vision_dim

        # Set projection head
        self.projection_head_vision = ProjectionLayer(layer=torch.nn.Linear(self.vision_dim, self.proj_dim,
                                                                            bias=proj_bias),
                                                      projection=projection, norm=norm)

    def forward(self, pixel_values):
        # Forwards trough vision encoder
        embed = self.model(pixel_values)

        # Compute projection from vision embedding to multi-modal projection
        embed = self.projection_head_vision(embed)
        return embed


class TextModel(torch.nn.Module):
    def __init__(self, bert_type='emilyalsentzer/Bio_ClinicalBERT', proj_dim=512, proj_bias=False, projection=True,
                 norm=True):
        super().__init__()

        # Set tokenizer，load from BERT
        self.tokenizer = AutoTokenizer.from_pretrained(bert_type)
        self.tokenizer.model_max_length = 77

        # Load text encoder from pretrained
        # load from huggingface
        self.model = AutoModel.from_pretrained(bert_type, output_hidden_states=True)

        # Set projection head
        # project from 768 -> 521
        self.projection_head_text = ProjectionLayer(layer=torch.nn.Linear(768, proj_dim, bias=proj_bias),
                                                    projection=projection, norm=norm)

    def tokenize(self, prompts_list):
        #create tokenizer
        # return_tensors='pt' represent（tensor）format。
        text_tokens = self.tokenizer(prompts_list, truncation=True, padding=True, return_tensors='pt')
        return text_tokens

    def forward(self, input_ids, attention_mask):

        # Forwards trough text encoder
        output = self.model(input_ids=input_ids, attention_mask=attention_mask)

        # Combine last feature layers to compute text embedding
        last_hidden_states = torch.stack([output['hidden_states'][1], output['hidden_states'][2],
                                          output['hidden_states'][-1]])
        embed = last_hidden_states.permute(1, 0, 2, 3).mean(2).mean(1)

        # Compute projection from text embedding to multi-modal projection
        embed = self.projection_head_text(embed)
        return embed


class ProjectionLayer(torch.nn.Module):
    def __init__(self, layer, projection=True, norm=True):
        super().__init__()

        self.apply_projection = projection
        self.norm_modality = bool(projection * norm)
        self.norm_projection = norm
        self.projection = layer

    def forward(self, x):

        if self.norm_modality:
            x = x / x.norm(dim=-1, keepdim=True)

        if self.apply_projection:
            x = self.projection(x)
            if self.norm_projection:
                x = x / x.norm(dim=-1, keepdim=True)

        return x
