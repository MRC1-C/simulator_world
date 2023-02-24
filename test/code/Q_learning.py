import torch.nn as nn
import torch
import numpy
class CNN(nn.Module):
    def __init__(self, dim_input=1, dim_output=1,kernel_size=3,padding =1, stride =1) -> None:
        super().__init__()  
        self.main=nn.Sequential(
            nn.Conv2d(dim_input,dim_output, kernel_size=kernel_size, padding=padding, stride=stride),
            nn.LeakyReLU(0.2),
            nn.MaxPool2d(2,2),
            nn.Flatten(),
            nn.Linear(4,2),
            nn.Tanh()
        )

    def forward(self,x):
        x = self.main(x)
        return x


