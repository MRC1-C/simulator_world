import torch.nn as nn
from .NetworkBase import CNN, RNN, Linear, AUTOENCODER, X
import torch 
class Model(nn.Module):
    def __init__(self,gens,modes,start_block=[], finish_block=[]) -> None:
        super().__init__()
        self.start_block = nn.Sequential(
            CNN(1,32,3,1,2),
            nn.Dropout()
        ) 

        self.finish_block = nn.Sequential(
            nn.Flatten(start_dim=1),
            nn.Linear(32**3, 100),
            nn.ReLU(),
            nn.Dropout(),
            nn.Linear(100,10),
            nn.Sigmoid()
        )
        self.batch_norm = nn.BatchNorm2d(32)
        self.dropout = nn.Dropout()
        self.layers = nn.ModuleList([])
        self.gens = gens
        self.modes = modes
        for gen in gens:
            self.layers.append(gen)
    def forward(self, x):
        xs = self.start_block(x)
        self.batch_norm(xs)
        for i in range(1, len(self.gens)-1):
            if self.modes[i-1] == "+":
                x1 = self.batch_norm(self.layers[i-1](xs)) 
                x2 = self.batch_norm(self.layers[i](self.batch_norm(self.start_block(x)))) 
                xs = x1 + x2
            else:
                x1 = self.batch_norm(self.layers[i-1](xs)) 
                x1 = self.dropout(x1)
                xs = self.layers[i-1](x1)
        self.batch_norm(xs)
        xs = self.finish_block(xs)
        return xs
    def setNullBlock(self):
        self.start_block = X()
        self.finish_block = X()