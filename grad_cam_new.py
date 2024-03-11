import os

os.environ['CUDA_VISIBLE_DEVICES'] = '1'
import torch
print(torch.cuda.device_count())

import urllib.request
import numpy as np
import torch
import torch.nn.functional as F
import matplotlib.pyplot as plt
import clip
from PIL import Image
from scipy.ndimage import filters
from torch import nn
from MDCLIP.modeling.model_with_rep import MDCLIP_with_rep
from MDCLIP.pretraining.data.transforms import LoadImage, ImageScaling, SelectRelevantKeys, CopyDict,\
    ProduceDescription, AugmentDescription
from torchvision.transforms import Compose
transforms_eval = Compose([
    CopyDict(),
    LoadImage(),
    ImageScaling()])


#Change your input of model_weight
model_wight = "resnet_v2100text_0weights_0perfor_nomore4-5_0-1_newRep_odir_other_lesssampling53bestmAP.pth"


model1 = MDCLIP_with_rep(vision_type='replknet', out_path="./local_data/results/pretraining/", from_checkpoint=True,
                    vision_pretrained=True, weights_path="./local_data/results/pretraining/"+model_wight
                    )

# @title Helper functions

# @markdown Some helper functions for overlaying heatmaps on top
# @markdown of images and visualizing with matplotlib.

def normalize(x: np.ndarray) -> np.ndarray:
    # Normalize to [0, 1].
    x = x - x.min()
    if x.max() > 0:
        x = x / x.max()
    return x


# Modified from: https://github.com/salesforce/ALBEF/blob/main/visualization.ipynb
def getAttMap(img, attn_map, blur=True):
    if blur:
        attn_map = filters.gaussian_filter(attn_map, 0.02 * max(img.shape[:2]))
    attn_map = normalize(attn_map)
    cmap = plt.get_cmap('jet')
    attn_map_c = np.delete(cmap(attn_map), 3, 2)
    attn_map = 1 * (1 - attn_map ** 0.7).reshape(attn_map.shape + (1,)) * img + \
               (attn_map ** 0.7).reshape(attn_map.shape + (1,)) * attn_map_c
    return attn_map


def viz_attn(img, attn_map,title, blur=True,):
    _, axes = plt.subplots(1, 2, figsize=(10, 5))
    axes[0].imshow(img)
    axes[1].imshow(getAttMap(img, attn_map, blur))
    for ax in axes:
        ax.axis("off")
    plt.title(title)
    plt.show()


def load_image(img_path, resize=None):
    image = Image.open(img_path).convert("RGB")
    if resize is not None:
        image = image.resize((resize, resize))
    return np.asarray(image).astype(np.float32) / 255.


# @title GradCAM: Gradient-weighted Class Activation Mapping

# @markdown Our gradCAM implementation registers a forward hook
# @markdown on the model at the specified layer. This allows us
# @markdown to save the intermediate activations and gradients
# @markdown at that layer.

# @markdown To visualize which parts of the image activate for
# @markdown a given caption, we use the caption as the target
# @markdown label and backprop through the network using the
# @markdown image as the input.
# @markdown In the case of CLIP models with resnet encoders,
# @markdown we save the activation and gradients at the
# @markdown layer before the attention pool, i.e., layer4.

class Hook:
    """Attaches to a module and records its activations and gradients."""

    def __init__(self, module: nn.Module):
        self.data = None
        self.hook = module.register_forward_hook(self.save_grad)

    def save_grad(self, module, input, output):
        self.data = output
        output.requires_grad_(True)
        output.retain_grad()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.hook.remove()

    @property
    def activation(self) -> torch.Tensor:
        return self.data

    @property
    def gradient(self) -> torch.Tensor:
        return self.data.grad


# Reference: https://arxiv.org/abs/1610.02391
def gradCAM(
        model: nn.Module,
        input: torch.Tensor,
        target: torch.Tensor,
        layer: nn.Module
) -> torch.Tensor:
    # Zero out any gradients at the input.
    if input.grad is not None:
        input.grad.data.zero_()

    # Disable gradient settings.
    requires_grad = {}
    for name, param in model.named_parameters():
        requires_grad[name] = param.requires_grad
        param.requires_grad_(False)

    # Attach a hook to the model at the desired layer.
    assert isinstance(layer, nn.Module)
    with Hook(layer) as hook:
        # Do a forward and backward pass.
        output = model(input)
        output.backward(target)

        grad = hook.gradient.float()
        act = hook.activation.float()

        # Global average pool gradient across spatial dimension
        # to obtain importance weights.
        alpha = grad.mean(dim=(2, 3), keepdim=True)
        # Weighted combination of activation maps over channel
        # dimension.
        gradcam = torch.sum(act * alpha, dim=1, keepdim=True)
        # We only want neurons with positive influence so we
        # clamp any negative ones.
        gradcam = torch.clamp(gradcam, min=0)

    # Resize gradcam to input resolution.
    gradcam = F.interpolate(
        gradcam,
        input.shape[2:],
        mode='bicubic',
        align_corners=False)

    # Restore gradient settings.
    for name, param in model.named_parameters():
        param.requires_grad_(requires_grad[name])

    return gradcam


# @title Run

# @markdown #### Image & Caption settings
image_url = 'https://images2.minutemediacdn.com/image/upload/c_crop,h_706,w_1256,x_0,y_64/f_auto,q_auto,w_1100/v1554995050/shape/mentalfloss/516438-istock-637689912.jpg'  # @param {type:"string"}

image_caption = 'the cat'  # @param {type:"string"}
# @markdown ---
# @markdown #### CLIP model settings
clip_model = "RN50"  # @param ["RN50", "RN101", "RN50x4", "RN50x16"]
#saliency_layer = "layer4"  # @param ["layer4", "layer3", "layer2", "layer1"]

saliency_layer = "layer4"  # @param ["layer4", "layer3", "layer2", "layer1"]
# @markdown ---
# @markdown #### Visualization settings
blur = True  # @param {type:"boolean"}

device = "cuda" if torch.cuda.is_available() else "cpu"
# model, preprocess = clip.load(clip_model, device=device, jit=False)

# Download the image from the web.
# image_path = 'image.png'
# urllib.request.urlretrieve(image_url, image_path)

#image_input = preprocess(Image.open(image_path)).unsqueeze(0).to(device)
#image_np = load_image(image_path, model1.visual.input_resolution)

# text_embeds_dict, text_embeds = model1.compute_text_embeddings(
#     ['normal', 'epiretinal membrane', 'macular edema', 'diabetic retinopathy',
#      'non-exudative age related macular degeneration', 'exudative age related macular degeneration',
#      'degenerative myopia'], domain_knowledge=False)


# text_embeds_dict, text_embeds = model1.compute_text_embeddings(
#     # ['diabetic retinopathy'], domain_knowledge=False)
image_name = "20200902_1415.fundus.jpg"
iamge_path = "./MDCLIP/Datasets/FUNDUS/topcon/fundus_512_oct_256/"+image_name
image_np = np.array(Image.open(iamge_path))
#text_embeds_dict, text_embeds = model1.compute_text_embeddings(['normal','epiretinal membrane', 'macular edema', 'diabetic retinopathy', 'non-exudative age related macular degeneration', 'exudative age related macular degeneration', 'degenerative myopia'],domain_knowledge=False)
image2 = Image.open(iamge_path).convert("RGB")
image3 = image2.resize((512, 512))
image4 = np.asarray(image3).astype(np.float32) / 255.

disease_name = "non-exudative age related macular degeneration"
text_embeds_dict, text_embeds = model1.compute_text_embeddings([disease_name],domain_knowledge=False)

x = model1.preprocess_image(image_np)

image = x.detach().clone()

text_input = clip.tokenize([image_caption]).to(device)

attn_map = gradCAM(
    model1.vision_model,
    torch.Tensor(image),
    text_embeds.float(),
    getattr(model1.vision_model.model.stages, "3")
)
attn_map = attn_map.squeeze().detach().cpu().numpy()

viz_attn(image4, attn_map,image_name + disease_name, blur)