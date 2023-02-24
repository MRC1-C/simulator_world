import torchvision.datasets as datasets
import torchvision.transforms as transforms
from torch.utils.data import DataLoader,Dataset,Subset
import torch
from model import NeuralNetwork
from config import device
from collections import Counter


transforms = transforms.Compose(
    [
        transforms.Resize((64,64)),
        transforms.ToTensor(),
    ]
)

training_data = datasets.MNIST(
    root="../data/dataMNIST",
    train=True,
    download=True,
    transform=transforms,
)

test_data = datasets.MNIST(
    root="../data/dataMNIST",
    train=False,
    download=True,
    transform=transforms,
)

class CustomDataset(Dataset):
    def __init__(self,cls):
        self.data = list(training_data)[:1000]
        self.cls = cls
    def __len__(self):
        return len(self.data)
    def __getitem__(self, idx):
        return self.data[idx][0],torch.Tensor([1,0]) if self.data[idx][1] == self.cls else torch.Tensor([0,1])

# def plot(data):

data = CustomDataset(1)
print(dict(Counter(str(dt[1]) for dt in data)))
# for i in range(10):
#     print(f'noron {i}')
#     batch_size = 64
#     data = CustomDataset(i)
#     train_dataloader = DataLoader(data, batch_size=batch_size)
#     model = NeuralNetwork()
#     model.train_model(train_dataloader,2)