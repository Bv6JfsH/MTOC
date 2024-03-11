"""
Methods for image and text loading, pre-processing and generation
for vision-language pretraining. Also, it includes data augmentation
utilities.
"""

import numpy as np
import random
import torch
import copy

from PIL import Image
from torchvision.transforms import Resize
from MDCLIP.modeling.dictionary import definitions
from kornia.augmentation import RandomHorizontalFlip, RandomAffine, ColorJitter, RandomResizedCrop, RandomGamma, RandomGaussianNoise, RandomHue, RandomSaturation, CenterCrop, ColorJiggle

# Augmentations for pretraining
# augmentations_pretraining = torch.nn.Sequential(RandomHorizontalFlip(p=0.25),
#                                                 RandomAffine(p=0.25, degrees=(-90, 90), scale=(0.9, 1)),
#                                                 RandomResizedCrop(p=0.25, size=(512, 512), scale=(0.25, 1.0)),
#                                                 ColorJitter(p=0.25, brightness=0.2, contrast=0.2, hue=0.2),
#                                                 RandomGamma(p=0.25, gamma=(0.8, 1.2)),
#                                                 RandomGaussianNoise(p=0.25, mean=0., std=1.)
#                                                 )


augmentations_pretraining = torch.nn.Sequential(RandomHorizontalFlip(p=0.5),
                                                RandomAffine(p=0.25, degrees=(-5, 5), scale=(0.9, 1)),
                                                ColorJitter(p=0.25, brightness=0.2, contrast=0.2))


class LoadImage():
    def __init__(self, target="image_path"):
        self.target = target
        """
        Load, organize channels, and standardize intensity of images.
        """

    def __call__(self, data):
        # Read image
        img = np.array(Image.open(data[self.target]), dtype=float)
        if np.max(img) > 1:
            img /= 255

        # channel first
        if len(img.shape) > 2:
            img = np.transpose(img, (2, 0, 1))
        else:
            img = np.expand_dims(img, 0)

        if img.shape[0] > 3:
            img = img[1:, :, :]
        if "image" in self.target:
            if img.shape[0] < 3:
                img = np.repeat(img, 3, axis=0)

        data[self.target.replace("_path", "")] = img
        return data


class ImageScaling():

    """
    Method for image scaling. It includes two options: scaling from canvas, to avoid image distortions,
    and regular scaling trough resizing.
    """

    def __init__(self, size=(512, 512), canvas=True, target="image"):
        self.size = size
        self.canvas = canvas
        self.target = target

        self.transforms = torch.nn.Sequential(
            Resize(self.size),
        )

    def __call__(self, data):
        img = torch.tensor(data[self.target])
        if not self.canvas or (img.shape[-1] == img.shape[-2]):
            img = self.transforms(img)
        else:
            sizes = img.shape[-2:]
            max_size = max(sizes)
            scale = max_size/self.size[0]
            img = Resize((int(img.shape[-2]/scale), int((img.shape[-1]/scale))))(img)
            img = torch.nn.functional.pad(img, (0, self.size[0] - img.shape[-1], 0, self.size[1] - img.shape[-2], 0, 0))

        data[self.target] = img
        return data


class ProduceDescription():

    """
    Method that creates naive text prompts combining a prompt template, atributes (e.g. noisy), and categories
    (e.g. cataract). Also, this method is used to integrate text data with the modality prompt template.
    """

    def __init__(self, caption):
        self.caption = caption

    def __call__(self, data):
        weights_map = {
            'normal':1,
            'a disease': 1, 'diabetic retinopathy':1, 'age-related macular degeneration':1,
            'media haze':2, 'drusens':3, 'myopia':1, 'branch retinal vein occlusion':3,
            'tessellation':3, 'epiretinal membrane':5, 'laser scar':3,
            'macular scar':10, 'central serous retinopathy':5, 'optic disc cupping':3,
            'central retinal vein occlusion':2, 'tortuous vessels':4, 'asteroid hyalosis':2,
            'optic disc pallor':7, 'optic disc edema':3, 'optociliary shunt vessels':20,
            'anterior ischemic optic neuropathy':20, 'parafoveal telangiectasia':20,
            'retinal traction':10, 'retinitis':2, 'chorioretinitis':5, 'exudation':5,
            'retinal pigment epithelium changes':10, 'macular hole':5,
            'retinitis pigmentosa':10, 'other':20,'glaucoma':3,'cataract':2,'hypertensive retinopathy':10,
            'other disease':1


        }

        # weights = [weights_map[element] for element in data['categories']]
        # Create text
        atr_sample = random.sample(data['atributes'], 1)[0] if len(data['atributes']) > 0 else ""
        cat_sample = random.sample(data['categories'], 1)[0] if len(data['categories']) > 0 else ""
        #cat_sample = random.choices(data['categories'], weights=weights, k=1)[0] if len(data['categories']) > 0 else ""
        data["sel_category"] = cat_sample
        data["report"] = [self.caption.replace("[ATR]",  atr_sample).replace("[CLS]",  cat_sample).replace("  ", " ")]

        return data


class AugmentDescription():

    """
    Method that augments naive text prompts into expert knowledge prompts by changing the category name
    by expert descriptions of the target category.
    """

    def __init__(self, augment=False):
        self.augment = augment

    def __call__(self, data):

        if self.augment:
            if data["image_name"].split("/")[0] not in ["06_EYENET", "11_STARE", "08_ODIR-5K", "31_JICHI"]:
                if data["sel_category"] in list(definitions.keys()):
                    prompts = [data["sel_category"]] + definitions[data["sel_category"]]
                    new_cat = random.sample(prompts, 1)[0]
                    data["report"][0] = data["report"][0].replace(data["sel_category"], new_cat)
                    data["augmented_category"] = new_cat

        return data


class CopyDict():
    def __call__(self, data):
        d = copy.deepcopy(data)
        return d


class SelectRelevantKeys():

    def __init__(self, target_keys=None):
        if target_keys is None:
            target_keys = ['image', 'report', 'sel_category', 'all_categories', 'labels']
        self.target_keys = target_keys

    def __call__(self, data):
        d = {key: data[key] for key in self.target_keys}
        return d

class AverageDescription():
    def __init__(self, average=False):
        self.average = average
    def __call__(self, data):

        if self.average:

            if data["sel_category"] in list(definitions.keys()):
                prompts = [data["sel_category"]] + definitions[data["sel_category"]]
                new_cat = random.sample(prompts, 1)[0]
                data["report"][0] = data["report"][0].replace(data["sel_category"], new_cat)
                data["augmented_category"] = new_cat

        return data