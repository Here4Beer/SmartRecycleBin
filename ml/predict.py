import torch
import numpy as np
from torchvision import transforms
from PIL import Image
import cv2


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
        self.class_names = [None, '3800048307881', '9008700147392', '80176800', '5449000131843']

    def predict(self, cv2_image):
        image = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        inputs = self.data_transforms(image)
        inputs = inputs.to(self.device)

        class_index = np.argmax(self.model(inputs[None, ...]).cpu().detach().numpy())
        return self.class_names[class_index]

