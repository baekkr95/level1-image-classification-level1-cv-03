import torch
from torchvision import transforms
from torch.utils.data import Dataset
<<<<<<< HEAD
from PIL import Image
=======

>>>>>>> 01780aff723488d48daace92a4aeb5e3c7053bce

class MaskDataset(Dataset):

    def __init__(self, input_data, output_data, transform):
        self.X = input_data
        self.Y = output_data
        self.transform = transform
        
    def __len__(self):
        return len(self.X)
        
    def __getitem__(self, index):
        image = self.transform(self.X[index])
        label = self.Y[index]
        return image, label


class TestDataset(Dataset):

    def __init__(self, img_paths, transform):
        self.img_paths = img_paths
        self.transform = transform

    def __getitem__(self, index):
        image = Image.open(self.img_paths[index])

        if self.transform:
            image = self.transform(image)
        return image

    def __len__(self):
        return len(self.img_paths)


class MultiMaskDataset(Dataset):

    def __init__(self, image_list, ismask, gender, age, transform):
        self.X = image_list
        self.ismask=ismask,
        self.gender=gender,
        self.age=age,
        
        self.transform = transform
        
    def __len__(self):
        return len(self.X)
        
    def __getitem__(self, index):
        image = self.transform(self.X[index])
        label = {
            'ismask':self.ismask[index],
            'gender':self.gender[index],
            'age':self.age[index],
        }
        return image, label

