import torch.nn as nn
import torch
device = "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"

class RNN(nn.Module):
    def __init__(self,seq_len=1024,D=2) -> None:
        super().__init__()  
        self.D = D
        self.hiden_len = int(seq_len/2) 
        self.rnn = nn.RNN(seq_len,int(seq_len/2) , bidirectional=(D==2),batch_first=True) 
        self.leaky = nn.LeakyReLU(0.2)
    def forward(self,x):
        x = torch.flatten(x, start_dim=2)
        h0 = torch.randn(self.D, x.shape[0],self.hiden_len)
        output, _ = self.rnn(x, h0.to(device))
        output = torch.reshape(output, (x.shape[0], x.shape[1],x.shape[1],x.shape[1]))
        return self.leaky(output)
