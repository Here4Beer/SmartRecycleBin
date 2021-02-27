import torch
import numpy as np
from torchvision import transforms
import os
from PIL import Image


class SmartBinPredictor:
    def __init__(self, model_path):
        self.model = torch.load(model_path)
        self.device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
        self.data_transforms = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ])
        self.class_names = ['Activia qgodka', 'Activia zakuska', 'Bravo', 'Nutella', 'koka']

    def predict(self, image_path: str):
        image = Image.open(image_path)
        inputs = self.data_transforms(image)
        inputs = inputs.to(self.device)

        return np.argmax(self.model(inputs[None, ...]).cpu().detach().numpy())

