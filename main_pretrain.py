
"""
Main function to pretrain MDCLIP model based on FLAIR using
an assembly dataset and vision-text modalities.
"""
import os

os.environ['CUDA_VISIBLE_DEVICES'] = '1' # GPU set
import argparse

import torch
print(torch.cuda.device_count())
from MDCLIP.modeling.misc import set_seeds
set_seeds(2024, use_cuda=torch.cuda.is_available())

from MDCLIP.pretraining.data.dataloader import get_loader
from MDCLIP.pretraining.data.transforms import augmentations_pretraining
from MDCLIP.modeling.model_with_rep import MDCLIP_with_rep
from MDCLIP.local_data.constants import *


def process(args):


    # Set data for val and test
    datalaoders = get_loader(dataframes_path=args.dataframes_path, data_root_path=args.data_root_path,
                             datasets=args.datasets, balance=args.balance, batch_size=args.batch_size,
                             num_workers=args.num_workers, banned_categories=args.banned_categories,
                             caption=args.caption, augment_description=args.augment_description,data_val=["RFMid_Validation_other"], data_test=["RFMid_Testing_other"])

    model = MDCLIP_with_rep(vision_type=args.architecture, out_path=args.out_path, from_checkpoint=False, vision_pretrained=True
                            )



#Train-test
    model.fit(datalaoders=datalaoders, epochs=args.epochs, lr=args.lr, weight_decay=args.weight_decay, scheduler=args.scheduler,
              warmup_epoch=args.warmup_epoch, store_num=args.store_num, transforms=augmentations_pretraining, record_name='100text_0weights_10perfor_newRep_topcon_Claude')





def main():
    parser = argparse.ArgumentParser()

    # Folders, data, etc.
    parser.add_argument('--data_root_path', default=PATH_DATASETS)
    parser.add_argument('--dataframes_path', default=PATH_DATAFRAME_PRETRAIN)
    parser.add_argument('--datasets',default=["RFMid_Training_other"])
    # parser.add_argument('--datasets', default=["RFMid_Training_other"])
                        # default=["topcon_train_more_4_5"])
                        # default=["topcon_final_train"])

    """
       01_EYEPACS , "03_IDRID", "04_RFMid", "05_1000x39",
                                               "06_EYENET", "07_LAG", "08_ODIR", "09_PAPILA", "10_PARAGUAY",
                                               "11_STARE", "12_ARIA", "14_AGAR300", "15_APTOS", "16_FUND-OCT",
                                               "17_DiaRetDB1", "18_DRIONS-DB", "19_Drishti-GS1",
                                               "20_E-ophta", "21_G1020", "23_HRF", "24_ORIGA", "26_ROC",
                                               "27_BRSET", "28_OIA-DDR", "29_AIROGS", "30_SUSTech-SYSU", "31_JICHI",
                                               "32_CHAKSU", "33_DR1-2", "34_Cataract", "35_ScarDat"])
    """
    parser.add_argument('--banned_categories', default=None)

    parser.add_argument('--out_path', default=PATH_RESULTS_PRETRAIN, help='output path')

    # Prompts setting and augmentation hyperparams
    parser.add_argument('--caption', default="A [ATR] fundus photograph of [CLS]")
    parser.add_argument('--augment_description', default=True, type=lambda x: (str(x).lower() == 'true'))

    # Dataloader setting
    parser.add_argument('--balance', default=True, type=lambda x: (str(x).lower() == 'true'))

    # Training options
    parser.add_argument('--epochs', default=15, type=int)
    parser.add_argument('--batch_size', default=16, type=int)
    parser.add_argument('--lr', default=1e-4, type=float, help='Learning rate')
    parser.add_argument('--weight_decay', default=1e-5, help='Weight Decay')
    parser.add_argument('--scheduler', default=True, type=lambda x: (str(x).lower() == 'true'))
    parser.add_argument('--warmup_epoch', default=1, type=int, help='number of warmup epochs')
    parser.add_argument('--store_num', default=50, type=int)

    # Architecture and pretrained weights options
    parser.add_argument('--architecture', default='replknet', help='resnet_v2 -- efficientnet -- replknet -- resnext -- densenet ')

    # Resources
    parser.add_argument('--num_workers', default=0, type=int, help='workers number for DataLoader')

    args, unknown = parser.parse_known_args()
    process(args=args)


if __name__ == "__main__":
    main()