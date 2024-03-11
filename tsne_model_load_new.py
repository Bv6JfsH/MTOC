import os
import torch
os.environ['CUDA_VISIBLE_DEVICES'] = '1'

import pandas as pd
import numpy as np
from torch.utils.data import  DataLoader
from MDCLIP.pretraining.data.dataset import Dataset, UniformDataset
from torchvision import transforms
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from MDCLIP.modeling.model_with_rep import MDCLIP_with_rep
from MDCLIP.pretraining.data.transforms import LoadImage, ImageScaling, SelectRelevantKeys, CopyDict,\
    ProduceDescription, AugmentDescription
from torchvision.transforms import Compose
transforms_eval = Compose([
    CopyDict(),
    LoadImage(),
    ImageScaling()])

# model1 = MDCLIP_with_rep(vision_type='resnet_v2', out_path="./local_data/results/pretraining/", from_checkpoint=True,
#                     vision_pretrained=True, weights_path="./local_data/results/pretraining/resnet_v2100text_0weights_0perfor_nomore4-5_0-1_newRep_rfmid_other_lesssampling55bestmAP.pth"
#                     )


model1 = MDCLIP_with_rep(vision_type='resnet_v2', out_path="./local_data/results/pretraining/", from_checkpoint=True,
                         vision_pretrained=True, weights_path="./local_data/results/pretraining/resnet_v2100text_0weights_10perfor_nomore4-5_0-1_newRep_rfmid_other_lesssampling55bestmAP.pth"
                         )
model1.eval()
model1.to('cpu')


# target_dict = {"normal": 0,
#                "epiretinal membrane": 1,
#                "macular edema": 2,
#                "diabetic retinopathy": 3,
#                "non-exudative age related macular degeneration": 4,
#                "exudative age related macular degeneration": 5,
#                "degenerative myopia": 6}

# target_dict = {
#     "normal": 0,
#                 # "a disease": 0,
#                "diabetic retinopathy": 1,
#                'age-related macular degeneration': 2,
#                'media haze': 3,
#                'drusens': 4,
#                'myopia': 5,
#                'branch retinal vein occlusion': 6,
#                'tessellation' :7,
#                'epiretinal membrane': 8,
#                'laser scar' : 9,
#                'macular scar' :10,
#                'central serous retinopathy' : 11,
#                'optic disc cupping': 12,
#                'central retinal vein occlusion' :13,
#                'tortuous vessels': 14,
#                'asteroid hyalosis': 15,
#                'optic disc pallor': 16,
#                'optic disc edema': 17,
#                'optociliary shunt vessels': 18,
#                'anterior ischemic optic neuropathy': 19,
#                'parafoveal telangiectasia': 20,
#                'retinal traction': 21,
#                'retinitis': 22,
#                'chorioretinitis': 23,
#                'exudation': 24,
#                'retinal pigment epithelium changes': 25,
#                'macular hole': 26,
#                'retinitis pigmentosa': 27,
#                'other': 28
#     # 'normal': 29
#                #'a disease': 0,
#                }

target_dict = {
    "normal": 0,
                # "a disease": 0,
               "diabetic retinopathy": 1,
               'age-related macular degeneration': 2,
               'media haze': 3,
               'drusens': 4,
               'myopia': 5,
               'branch retinal vein occlusion': 6,
               'tessellation' :7,
               'epiretinal membrane': 8,
               'laser scar' : 9,
               'macular scar' :10,
               'central serous retinopathy' : 11,
               'optic disc cupping': 12,
               'central retinal vein occlusion' :13,
               'tortuous vessels': 14,
               'asteroid hyalosis': 15,
               'optic disc pallor': 16,
               'optic disc edema': 17
               }

data = []
for iDataset in ["RFMid_Testing_other"]:
    print("Processing data: " + iDataset)

    dataframe = pd.read_csv("./MDCLIP/local_data/dataframes/pretraining/" + iDataset + ".csv")

    for i in range(len(dataframe)):
        data_i = dataframe.loc[i, :].to_dict()
        data_i["all_categories"] = data_i["categories"]
        data_i["categories"] = eval(data_i["categories"])
        data_i["atributes"] = eval(data_i["atributes"])



        data_i["image_name"] = data_i["image"]
        data_i["image_path"] = "./MDCLIP/Datasets/FUNDUS/" + data_i["image"]
        if not any(element in data_i["categories"] for element in target_dict.keys()):
            continue
        labels_list = [target_dict[i] for i in data_i["categories"] if i in target_dict.keys()]
        data_i["labels"] = [1 if i in labels_list else 0 for i in range(18)]
        data_i["categories"] = []
        data.append(data_i)

print('Total assembly data samples: {}'.format(len(data)))
test_dataset = Dataset(data=data, transform=transforms_eval)
test_loader = DataLoader(test_dataset, batch_size=12, shuffle=False, num_workers=10)









X_images = np.zeros((0, 512))
y_labels = np.zeros((0, 18))

for step, batch in enumerate(test_loader):
    # batch_images = batch["image"].view(batch["image"].size(0), -1).numpy()
    images = batch["image"].to(torch.float32)

    img_embeds = model1.vision_model(images)

    norm = torch.norm(img_embeds, p=2)
    img_embeds_2 = img_embeds/norm

    img_embeds_1 = img_embeds_2.detach().numpy()
    X_images = np.vstack([X_images, img_embeds_1])
    y = np.stack(batch["labels"],axis=1)
    y_labels = np.vstack([y_labels, y])

t_features = []
t_labels = []

for i in range(len(X_images)):
    label_indices = np.where(y_labels[i] == 1)[0]
    for label_index in label_indices:
        t_features.append(X_images[i])
        t_labels.append(label_index)


input_tsne = np.vstack(t_features)
label_tsne = np.array(t_labels)


tsne = TSNE(n_components=2, random_state=42)
X_tsne = tsne.fit_transform(input_tsne)


plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=label_tsne, cmap='tab20c')
plt.title('t-SNE Visualization of Multi-label Data')

plt.colorbar(label='Class Index')
plt.show()