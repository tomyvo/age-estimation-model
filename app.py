import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import math



_weights_dict = dict()

def load_weights(weight_file):
    if weight_file == None:
        return

    try:
        weights_dict = np.load(weight_file, allow_pickle=True).item()
    except:
        weights_dict = np.load(weight_file, allow_pickle=True, encoding='bytes').item()

    return weights_dict

class KitModel(nn.Module):

    
    def __init__(self, weight_file):
        super(KitModel, self).__init__()
        global _weights_dict
        _weights_dict = load_weights(weight_file)

        self.conv1_1 = self.__conv(2, name='conv1_1', in_channels=3, out_channels=64, kernel_size=(3, 3), stride=(1, 1), groups=1, bias=True)
        self.conv1_2 = self.__conv(2, name='conv1_2', in_channels=64, out_channels=64, kernel_size=(3, 3), stride=(1, 1), groups=1, bias=True)
        self.conv2_1 = self.__conv(2, name='conv2_1', in_channels=64, out_channels=128, kernel_size=(3, 3), stride=(1, 1), groups=1, bias=True)
        self.conv2_2 = self.__conv(2, name='conv2_2', in_channels=128, out_channels=128, kernel_size=(3, 3), stride=(1, 1), groups=1, bias=True)
        self.conv3_1 = self.__conv(2, name='conv3_1', in_channels=128, out_channels=256, kernel_size=(3, 3), stride=(1, 1), groups=1, bias=True)
        self.conv3_2 = self.__conv(2, name='conv3_2', in_channels=256, out_channels=256, kernel_size=(3, 3), stride=(1, 1), groups=1, bias=True)
        self.conv3_3 = self.__conv(2, name='conv3_3', in_channels=256, out_channels=256, kernel_size=(3, 3), stride=(1, 1), groups=1, bias=True)
        self.conv4_1 = self.__conv(2, name='conv4_1', in_channels=256, out_channels=512, kernel_size=(3, 3), stride=(1, 1), groups=1, bias=True)
        self.conv4_2 = self.__conv(2, name='conv4_2', in_channels=512, out_channels=512, kernel_size=(3, 3), stride=(1, 1), groups=1, bias=True)
        self.conv4_3 = self.__conv(2, name='conv4_3', in_channels=512, out_channels=512, kernel_size=(3, 3), stride=(1, 1), groups=1, bias=True)
        self.conv5_1 = self.__conv(2, name='conv5_1', in_channels=512, out_channels=512, kernel_size=(3, 3), stride=(1, 1), groups=1, bias=True)
        self.conv5_2 = self.__conv(2, name='conv5_2', in_channels=512, out_channels=512, kernel_size=(3, 3), stride=(1, 1), groups=1, bias=True)
        self.conv5_3 = self.__conv(2, name='conv5_3', in_channels=512, out_channels=512, kernel_size=(3, 3), stride=(1, 1), groups=1, bias=True)
        self.fc6_1 = self.__dense(name = 'fc6_1', in_features = 25088, out_features = 4096, bias = True)
        self.fc7_1 = self.__dense(name = 'fc7_1', in_features = 4096, out_features = 4096, bias = True)
        self.fc8_101_1 = self.__dense(name = 'fc8-101_1', in_features = 4096, out_features = 101, bias = True)

    def forward(self, x):
        conv1_1_pad     = F.pad(x, (1, 1, 1, 1))
        conv1_1         = self.conv1_1(conv1_1_pad)
        relu1_1         = F.relu(conv1_1)
        conv1_2_pad     = F.pad(relu1_1, (1, 1, 1, 1))
        conv1_2         = self.conv1_2(conv1_2_pad)
        relu1_2         = F.relu(conv1_2)
        pool1_pad       = F.pad(relu1_2, (0, 1, 0, 1), value=float('-inf'))
        pool1, pool1_idx = F.max_pool2d(pool1_pad, kernel_size=(2, 2), stride=(2, 2), padding=0, ceil_mode=False, return_indices=True)
        conv2_1_pad     = F.pad(pool1, (1, 1, 1, 1))
        conv2_1         = self.conv2_1(conv2_1_pad)
        relu2_1         = F.relu(conv2_1)
        conv2_2_pad     = F.pad(relu2_1, (1, 1, 1, 1))
        conv2_2         = self.conv2_2(conv2_2_pad)
        relu2_2         = F.relu(conv2_2)
        pool2_pad       = F.pad(relu2_2, (0, 1, 0, 1), value=float('-inf'))
        pool2, pool2_idx = F.max_pool2d(pool2_pad, kernel_size=(2, 2), stride=(2, 2), padding=0, ceil_mode=False, return_indices=True)
        conv3_1_pad     = F.pad(pool2, (1, 1, 1, 1))
        conv3_1         = self.conv3_1(conv3_1_pad)
        relu3_1         = F.relu(conv3_1)
        conv3_2_pad     = F.pad(relu3_1, (1, 1, 1, 1))
        conv3_2         = self.conv3_2(conv3_2_pad)
        relu3_2         = F.relu(conv3_2)
        conv3_3_pad     = F.pad(relu3_2, (1, 1, 1, 1))
        conv3_3         = self.conv3_3(conv3_3_pad)
        relu3_3         = F.relu(conv3_3)
        pool3_pad       = F.pad(relu3_3, (0, 1, 0, 1), value=float('-inf'))
        pool3, pool3_idx = F.max_pool2d(pool3_pad, kernel_size=(2, 2), stride=(2, 2), padding=0, ceil_mode=False, return_indices=True)
        conv4_1_pad     = F.pad(pool3, (1, 1, 1, 1))
        conv4_1         = self.conv4_1(conv4_1_pad)
        relu4_1         = F.relu(conv4_1)
        conv4_2_pad     = F.pad(relu4_1, (1, 1, 1, 1))
        conv4_2         = self.conv4_2(conv4_2_pad)
        relu4_2         = F.relu(conv4_2)
        conv4_3_pad     = F.pad(relu4_2, (1, 1, 1, 1))
        conv4_3         = self.conv4_3(conv4_3_pad)
        relu4_3         = F.relu(conv4_3)
        pool4_pad       = F.pad(relu4_3, (0, 1, 0, 1), value=float('-inf'))
        pool4, pool4_idx = F.max_pool2d(pool4_pad, kernel_size=(2, 2), stride=(2, 2), padding=0, ceil_mode=False, return_indices=True)
        conv5_1_pad     = F.pad(pool4, (1, 1, 1, 1))
        conv5_1         = self.conv5_1(conv5_1_pad)
        relu5_1         = F.relu(conv5_1)
        conv5_2_pad     = F.pad(relu5_1, (1, 1, 1, 1))
        conv5_2         = self.conv5_2(conv5_2_pad)
        relu5_2         = F.relu(conv5_2)
        conv5_3_pad     = F.pad(relu5_2, (1, 1, 1, 1))
        conv5_3         = self.conv5_3(conv5_3_pad)
        relu5_3         = F.relu(conv5_3)
        pool5_pad       = F.pad(relu5_3, (0, 1, 0, 1), value=float('-inf'))
        pool5, pool5_idx = F.max_pool2d(pool5_pad, kernel_size=(2, 2), stride=(2, 2), padding=0, ceil_mode=False, return_indices=True)
        fc6_0           = pool5.view(pool5.size(0), -1)
        fc6_1           = self.fc6_1(fc6_0)
        relu6           = F.relu(fc6_1)
        drop6           = F.dropout(input = relu6, p = 0.5, training = self.training, inplace = False)
        fc7_0           = drop6.view(drop6.size(0), -1)
        fc7_1           = self.fc7_1(fc7_0)
        relu7           = F.relu(fc7_1)
        drop7           = F.dropout(input = relu7, p = 0.5, training = self.training, inplace = False)
        fc8_101_0       = drop7.view(drop7.size(0), -1)
        fc8_101_1       = self.fc8_101_1(fc8_101_0)
        prob            = F.softmax(fc8_101_1, dim=1)
        return prob


    @staticmethod
    def __dense(name, **kwargs):
        layer = nn.Linear(**kwargs)
        layer.state_dict()['weight'].copy_(torch.from_numpy(_weights_dict[name]['weights']))
        if 'bias' in _weights_dict[name]:
            layer.state_dict()['bias'].copy_(torch.from_numpy(_weights_dict[name]['bias']))
        return layer

    @staticmethod
    def __conv(dim, name, **kwargs):
        if   dim == 1:  layer = nn.Conv1d(**kwargs)
        elif dim == 2:  layer = nn.Conv2d(**kwargs)
        elif dim == 3:  layer = nn.Conv3d(**kwargs)
        else:           raise NotImplementedError()

        layer.state_dict()['weight'].copy_(torch.from_numpy(_weights_dict[name]['weights']))
        if 'bias' in _weights_dict[name]:
            bias = _weights_dict[name]['bias']
            bias = np.squeeze(bias)  # 4D → 1D
            layer.state_dict()['bias'].copy_(torch.from_numpy(bias))
        return layer

# =======================================================
# 🔍 UTKFace Evaluation + Custom Image Prediction (mit Face-Cropping)
# =======================================================

import os
import torch
import torch.nn as nn
from tqdm import tqdm
from torch.utils.data import Dataset, DataLoader
import torchvision.transforms as transforms
from PIL import Image
import pandas as pd
import numpy as np
import gradio as gr
from mtcnn import MTCNN

# ---------------------------
# 1️⃣ Pfade & Parameter
# ---------------------------
MODEL_WEIGHT = 'pytorch_model.pth'
UTKFACE_DIR = ''
CUSTOM_DIR = ''  # deine Testbilder hier
BATCH_SIZE = 32
NUM_WORKERS = 2
TOLERANCE = 5  # Jahre für Accuracy ±TOLERANCE

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# ---------------------------
# 2️⃣ Modell laden
# ---------------------------
model = KitModel(weight_file=MODEL_WEIGHT)
model.eval()
model.to(device)

# ---------------------------
# 3️⃣ Face Detector (MTCNN)
# ---------------------------
detector = MTCNN()

def crop_face_mtcnn(img_input):
    # img_input kann Pfad oder PIL.Image sein
    if isinstance(img_input, str):
        img = Image.open(img_input).convert('RGB')
    else:
        img = img_input.convert('RGB')

    img_np = np.array(img)
    faces = detector.detect_faces(img_np)
    if not faces:
        return img  # kein Gesicht gefunden → Originalbild
    x, y, w, h = faces[0]['box']
    face = img.crop((x, y, x + w, y + h))
    return face

# ---------------------------
# 4️⃣ Transformation
# ---------------------------
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

mean = torch.tensor([103.939, 116.779, 123.68]).view(3,1,1)

# ---------------------------
# 5️⃣ UTKFace Dataset (mit Label)
# ---------------------------
class UTKFaceDataset(Dataset):
    def __init__(self, image_dir):
        self.image_dir = image_dir
        self.filenames = [f for f in os.listdir(image_dir) if f.lower().endswith(('.jpg','.jpeg','.png'))]

    def __len__(self):
        return len(self.filenames)

    def __getitem__(self, idx):
        fname = self.filenames[idx]
        age = int(fname.split('_')[0])
        img_path = os.path.join(self.image_dir, fname)

        img = crop_face_mtcnn(img_path)  # 🟢 Gesichts-Crop hier
        img_tensor = transform(img) * 255
        img_tensor = img_tensor[[2,1,0], :, :]  # RGB → BGR
        img_tensor = img_tensor - mean
        return img_tensor, age, fname

# ---------------------------
# 6️⃣ Custom Dataset (ohne Label)
# ---------------------------
class CustomFaceDataset(Dataset):
    def __init__(self, image_files):
        """
        image_files: Liste von Dateipfaden oder PIL-Bildern aus Gradio
        """
        self.image_files = image_files

    def __len__(self):
        return len(self.image_files)

    def __getitem__(self, idx):
        file = self.image_files[idx]
        if isinstance(file, str):
            img = Image.open(file).convert("RGB")
            fname = os.path.basename(file)
        else:
            img = Image.open(file.name).convert("RGB")
            fname = os.path.basename(file.name)

        img = crop_face_mtcnn(img)
        img_tensor = transform(img) * 255
        img_tensor = img_tensor[[2, 1, 0], :, :]
        img_tensor = img_tensor - mean
        return img_tensor, fname
    
def predict_age(files):
    dataset = CustomFaceDataset(files)
    loader = DataLoader(dataset, batch_size=1, shuffle=False)

    results = []
    display_imgs = []

    with torch.inference_mode():
        for i, (imgs, fnames) in enumerate(loader):
            imgs = imgs.to(device)
            outputs = model(imgs)
            pred_age = int(outputs.argmax(dim=1).item())
            results.append({"Filename": fnames[0], "Predicted Age": pred_age})

            # 🔧 Richtige Bildquelle finden
            file = files[i]  # passendes hochgeladenes Bild
            img = Image.open(file.name).convert("RGB")
            cropped = crop_face_mtcnn(img)
            display_imgs.append((cropped, f"Predicted Age: {pred_age}"))

    df = pd.DataFrame(results)
    return display_imgs, df

with gr.Blocks(theme=gr.themes.Soft(), title="Age Estimation App") as demo:
    gr.Markdown("## 👵 Age Estimation with Face Cropping")

    with gr.Row():
        file_input = gr.File(
            label="Upload one or more images",
            file_count="multiple",
            file_types=["image"],
        )

    predict_button = gr.Button("🔍 Predict Age", variant="primary")

    gallery_output = gr.Gallery(
        label="Predictions", show_label=False, columns=[3], height="auto"
    )
    df_output = gr.Dataframe(label="Results Table", interactive=False)

    predict_button.click(
        fn=predict_age,
        inputs=file_input,
        outputs=[gallery_output, df_output],
    )

if __name__ == "__main__":
    demo.launch()