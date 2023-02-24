import torch.nn as nn
import torch
class AUTOENCODER(nn.Module):
    def __init__(self, dim_input=32, dim_output=32,kernel_size=3,padding =1, stride =2) -> None:
        super().__init__()  
        self.encoder=nn.Sequential(
            nn.Conv2d(dim_input,dim_output, kernel_size=kernel_size, padding=padding, stride=stride),
            nn.LeakyReLU(0.2),
            nn.Conv2d(dim_input,dim_output, kernel_size=kernel_size, padding=padding, stride=stride),
            nn.LeakyReLU(0.2),
        )
        self.decoder = nn.Sequential(
            nn.ConvTranspose2d(dim_input, dim_output,2,2,0),
            nn.LeakyReLU(0.2),
            nn.ConvTranspose2d(dim_input, dim_output,2,2,0),
            nn.LeakyReLU(0.2),
        )
    def forward(self,x):
        x = self.encoder(x)
        x = self.decoder(x)
        return x

# input = torch.randn(32,32,32)
# a = AUTOENCODER()
# print(a(input).shape)