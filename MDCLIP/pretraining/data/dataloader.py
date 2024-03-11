"""
Dataset and Dataloader preparation for vision-language pre-training
"""

import pandas as pd

from torchvision.transforms import Compose
from torch.utils.data import DataLoader

from MDCLIP.pretraining.data.dataset import Dataset, UniformDataset
from MDCLIP.pretraining.data.transforms import LoadImage, ImageScaling, SelectRelevantKeys, CopyDict,\
    ProduceDescription, AugmentDescription


def get_loader(dataframes_path, data_root_path, datasets, balance=False, batch_size=8, num_workers=0,
               banned_categories=None, caption="A fundus photograph of [CLS]", augment_description=True, data_val=None, data_test=None):


    target_dict = {"normal": 0,
                "epiretinal membrane": 1,
                "macular edema": 2,
                "diabetic retinopathy": 3,
                "non-exudative age related macular degeneration": 4,
                "exudative age related macular degeneration": 5,
                "degenerative myopia": 6}

    # target_dict = {"normal": 0,
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
    #                'tortuous vessels':14,
    #                'asteroid hyalosis':15,
    #                'optic disc pallor' :16,
    #                'optic disc edema' :17,
    #                'shunt':18,
    #                 'anterior ischemic optic neuropathy':19,
    #                'parafoveal telangiectasia' :20,
    #                'retinal traction' : 21,
    #                'retinitis': 22,
    #                'chorioretinitis': 23,
    #                'edudates': 24,
    #                'retinal pigment epithelium changes' :25,
    #                'macular hole' :26,
    #                'retinitis pigmentosa' :27 ,
    #                'cotton wool spots' :28 ,
    #                'colobomas':29,
    #                 'optic disc pit maculopathy':30,
    #                'preretinal haemorrhage':31,
    #                'myelinated nerve fibers' :32,
    #                'haemorrhagic retinopathy' :33,
    #                 'central retinal artery occlusion':34,
    #                'tilted disc' :35,
    #                'cystoid macular edema' :36,
    #                'post traumatic choroidal rupture':37,
    #                'choroidal folds' :38,
    #                'vitreous haemorrhage' :39,
    #                'macroaneurysm' :40,
    #                 'vasculitis' :41,
    #                'branch retinal artery occlusion' :42,
    #                'plaque' :43,
    #                'haemorrhagic pigment epithelial detachment':44,
    #                'collaterals':45
    #                }



    # target_dict = {
    #     # "normal": 0,
    #                 "a disease": 0,
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
    #                'other': 28,
    #     'normal': 29
    #                #'a disease': 0,
    #                }

    # target_dict = {
    # "a disease": 0,
    #                "diabetic retinopathy": 1,
    #                'age-related macular degeneration': 2,
    #                'media haze': 3,
    #                'drusens': 4,
    #                'myopia': 5,
    #                'branch retinal vein occlusion': 6,
    #                'tessellation': 7,
    #                'epiretinal membrane': 8,
    #                'laser scar': 9,
    #                'macular scar': 10,
    #                'central serous retinopathy': 11,
    #                'optic disc cupping': 12,
    #                'central retinal vein occlusion':13,
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
    #                'other': 28,
    #                'cotton wool spots' :47 ,
    #                'colobomas': 29,
    #                 'optic disc pit maculopathy':30,
    #                'preretinal haemorrhage':31,
    #                'myelinated nerve fibers' :32,
    #                'haemorrhagic retinopathy' :33,
    #                 'central retinal artery occlusion':34,
    #                'tilted disc' : 35,
    #                'cystoid macular edema':36,
    #                'post traumatic choroidal rupture':37,
    #                'choroidal folds' :38,
    #                'vitreous haemorrhage' :39,
    #                'macroaneurysm' :40,
    #                 'vasculitis' :41,
    #                'branch retinal artery occlusion' :42,
    #                'plaque' :43,
    #                'haemorrhagic pigment epithelial detachment':44,
    #                'collaterals':45,
    #         'normal': 46
    # }

#     target_dict = {
#         "normal":0,
# "diabetic retinopathy":1,
#         "glaucoma":2,
#         "cataract":3,
#         "age-related macular degeneration":4,
#         "hypertensive retinopathy":5,
#         "myopia":6,
#         "other disease":7
#     }



    # Prepare data sample pre-processing transforms，
    transforms = Compose([
        CopyDict(),
        LoadImage(),
        ImageScaling(),
        ProduceDescription(caption=caption),
        AugmentDescription(augment=augment_description),
        SelectRelevantKeys()
    ])

    transforms_eval = Compose([
        CopyDict(),
        LoadImage(),
        ImageScaling()])

    # Assembly dataframes into a combined data structure
    print("Setting assebly data...")
    data = []
    for iDataset in datasets:
        print("Processing data: " + iDataset)

        dataframe = pd.read_csv(dataframes_path + iDataset + ".csv")

        for i in range(len(dataframe)):
            data_i = dataframe.loc[i, :].to_dict()
            data_i["all_categories"] = data_i["categories"]
            data_i["categories"] = eval(data_i["categories"])
            data_i["atributes"] = eval(data_i["atributes"])

            # Remove banned words - for evaluating on incremental categories
            # banned = False
            # if banned_categories is not None:
            #     for iCat in data_i["categories"]:
            #         for iiCat in banned_categories:
            #             if iiCat in iCat:
            #                 banned = True
            # if banned:
            #     continue

            # Add sample to general data
            data_i["image_name"] = data_i["image"]
            data_i["image_path"] = data_root_path + data_i["image"]
            labels_list = [target_dict[i] for i in data_i["categories"]]

            data_i["labels"] = [1 if i in labels_list else 0 for i in range(46)]


            data.append(data_i)

    print('Total assembly data samples: {}'.format(len(data)))

    # Set data
    if balance:
        train_dataset = UniformDataset(data=data, transform=transforms)
    else:
        train_dataset = Dataset(data=data, transform=transforms)

    # Set dataloader
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True, num_workers=num_workers)


    #
    data = []
    for iDataset in data_val:
        print("Processing data: " + iDataset)

        dataframe = pd.read_csv(dataframes_path + iDataset + ".csv")

        for i in range(len(dataframe)):
            data_i = dataframe.loc[i, :].to_dict()
            data_i["all_categories"] = data_i["categories"]
            data_i["categories"] = eval(data_i["categories"])
            data_i["atributes"] = eval(data_i["atributes"])

            # Add sample to general data
            data_i["image_name"] = data_i["image"]
            data_i["image_path"] = data_root_path + data_i["image"]
            labels_list = [target_dict[i] for i in data_i["categories"]]

            data_i["labels"] = [1 if i in labels_list else 0 for i in range(46)]
            data_i["categories"] = []
            data.append(data_i)

    print('Total assembly data samples: {}'.format(len(data)))
    val_dataset = Dataset(data=data, transform=transforms_eval)
    val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False, num_workers=num_workers)




    data = []
    for iDataset in data_test:
        print("Processing data: " + iDataset)

        dataframe = pd.read_csv(dataframes_path + iDataset + ".csv")

        for i in range(len(dataframe)):
            data_i = dataframe.loc[i, :].to_dict()
            data_i["all_categories"] = data_i["categories"]
            data_i["categories"] = eval(data_i["categories"])
            data_i["atributes"] = eval(data_i["atributes"])


            # Add sample to general data
            data_i["image_name"] = data_i["image"]
            data_i["image_path"] = data_root_path + data_i["image"]
            labels_list = [target_dict[i] for i in data_i["categories"]]
            data_i["labels"] = [1 if i in labels_list else 0 for i in range(46)]
            data_i["categories"] = []
            data.append(data_i)

    print('Total assembly data samples: {}'.format(len(data)))
    test_dataset = Dataset(data=data, transform=transforms_eval)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False, num_workers=num_workers)




    data = []
    for iDataset in datasets:
        print("Processing data: " + iDataset)

        dataframe = pd.read_csv(dataframes_path + iDataset + ".csv")

        for i in range(len(dataframe)):
            data_i = dataframe.loc[i, :].to_dict()
            data_i["all_categories"] = data_i["categories"]
            data_i["categories"] = eval(data_i["categories"])
            data_i["atributes"] = eval(data_i["atributes"])



            # Add sample to general data
            data_i["image_name"] = data_i["image"]
            data_i["image_path"] = data_root_path + data_i["image"]
            labels_list = [target_dict[i] for i in data_i["categories"]]
            data_i["labels"] = [1 if i in labels_list else 0 for i in range(46)]
            data_i["categories"] = []
            data.append(data_i)

    print('Total assembly data samples: {}'.format(len(data)))
    train_eval_dataset = Dataset(data=data, transform=transforms_eval)
    train_eval_loader = DataLoader(train_eval_dataset, batch_size=batch_size, shuffle=False, num_workers=num_workers)





    # Set dataloaders in dict
    datalaoders = {"train": train_loader, "val": val_loader, "test": test_loader, "train_eval": train_eval_loader}

    # datalaoders = {"train": train_loader}
    return datalaoders
