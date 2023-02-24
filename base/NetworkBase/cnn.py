import torch.nn as nn
import torch
class CNN(nn.Module):
    def __init__(self, dim_input=32, dim_output=32,kernel_size=3,padding =1, stride =1) -> None:
        super().__init__()  
        self.main=nn.Sequential(
            nn.Conv2d(dim_input,dim_output, kernel_size=kernel_size, padding=padding, stride=stride),
            nn.LeakyReLU(0.2),
            nn.Conv2d(32,32,3,1,1),
            nn.LeakyReLU(0.2),
            # nn.MaxPool2d(2,2)
        )


    def forward(self,x):
        x = self.main(x)
        return x

# input = torch.randn(32,32,32)
# a = CNN()
# print(a(input).shape)