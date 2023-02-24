import torch 
import torch.nn as nn


input = torch.randn(32,32,32)

a = nn.ConvTranspose2d(32,32,2,2,0)

print(a(input).shape)