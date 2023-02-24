import torch.nn as nn
# from .config import OUTPUT_BASE
import torch

class Linear(nn.Module):
    def __init__(self, input_size=32, output_size=32) -> None:
        super().__init__()  
        self.output_size = output_size
        self.main=nn.Sequential(
            nn.Flatten(start_dim=1),
            nn.Linear(input_size**3, input_size**3),
            nn.LeakyReLU(0.2),
        )
    def forward(self,x):
        x = self.main(x)
        return x.reshape(x.shape[0], self.output_size,self.output_size,self.output_size)

