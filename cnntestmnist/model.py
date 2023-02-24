from torch import nn
import torch
from config import device
class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.main = nn.Sequential(
            nn.Conv2d(1,30,3,1,1),
            nn.LeakyReLU(0.2),
            nn.MaxPool2d(2,2),
            nn.BatchNorm2d(30),

            nn.Conv2d(30,30,3,1,1),
            nn.MaxPool2d(2,2),
            nn.BatchNorm2d(30),
            nn.LeakyReLU(0.2),

            nn.Conv2d(30,30,3,1,1),
            nn.LeakyReLU(0.2),
            nn.MaxPool2d(2,2),
            nn.BatchNorm2d(30),

            nn.Conv2d(30,30,3,1,1),
            nn.LeakyReLU(0.2),
            nn.MaxPool2d(2,2),
            nn.BatchNorm2d(30),

            nn.Flatten(),
            nn.Linear(30*4*4, 100),
            nn.ReLU(),
            nn.Linear(100, 2)
        )
        self.loss_fn = nn.CrossEntropyLoss()
        self.optimizer = torch.optim.SGD(self.parameters(), lr=1e-3)
        # for i in range(epoch):
    def forward(self, x):
        return self.main(x)
    def train_model(self,dataloader,epochs=3):
        for i in range(epochs):
            print(f'epoch {i+1}/{epochs}')
            size = len(dataloader.dataset)
            self.train()
            for batch, (X, y) in enumerate(dataloader):
                X, y = X.to(device), y.to(device)

                pred = self(X)
                loss = self.loss_fn(pred, y)

                self.optimizer.zero_grad()
                loss.backward()
                self.optimizer.step()
                loss, current = loss.item(), batch * len(X)
                print(f"loss: {loss:>7f}  [{current:>5d}/{size:>5d}]")
