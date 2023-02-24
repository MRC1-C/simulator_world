from .NetworkBase import CNN, RNN, AUTOENCODER, X
from .train_children import train
from .test_children import test
import torch.nn as nn
import torch
import random
import matplotlib.pyplot as plt
from .create_model import Model
import pymongo
import json
import gridfs
from .genv_to_image import draw_grapt
NNs = [CNN(),RNN(), AUTOENCODER(),X()]
modes = ["+","-"]

class Base:
    def __init__(self, gen, mode,genv,energy=10, loss=nn.CrossEntropyLoss(), lr=1e-3,device='cpu') -> None:
        self.gen = gen
        self.mode = mode
        self.energy = energy
        self.loss = loss
        self.lr = lr
        self.genv = genv
        self.epoch_train = 0
        self.device = device
        self.loss_train = []
        self.loss_test = []
        self.acc = []
        self.x = []
        # self.vgens = []
        # self.vmode = []
    def reproduction(self,device):
        if random.random() < 0.3:
            self.mutation()
        self.model = Model(self.gen, self.mode).to(device)
        self.opt = torch.optim.SGD(self.model.parameters(), lr=1e-3)
        self.param = sum(p.numel() for p in self.model.parameters() if p.requires_grad)
        self.id = id(self.model)
        print(self.genv)
        return self
    def mutation(self):
        random.shuffle(NNs)
        random.shuffle(modes)
        self.gen.append(NNs[0])
        self.mode.append(modes[0])
        self.genv = self.genv + " " + modes[0] + " " + NNs[0].__class__.__name__
    def train(self,data_train=[]):
        loss_train = train(self.model,self.loss,self.opt,data_train=data_train,device=self.device)
        self.loss_train.append(loss_train) 
        self.epoch_train +=1
        self.x.append(self.epoch_train)
    def test(self,data_test=[]):
        loss_test,acc =  test(data_test, self.model,self.loss,device=self.device)
        self.loss_test.append(loss_test)
        self.acc.append(acc)
        return acc
    def plot(self):
        plt.figure(figsize=(5, 2.7))
        plt.plot(self.x, self.loss_train, label='train')  
        plt.plot(self.x, self.loss_test, label='test') 
        plt.xlabel('epoch')
        plt.ylabel('loss')
        plt.legend()
        plt.savefig('children{}.png'.format(self.id))
        plt.show()
    def save(self):
        torch.save({
                'model_state_dict': self.model.state_dict(),
                'optimizer_state_dict': self.opt.state_dict(),
            },f'model{self.id}.pt')
        client = pymongo.MongoClient('mongodb+srv://CJ:1234@cluster0.uuqiy.mongodb.net/?retryWrites=true&w=majority')
        db = client.test_database
        models = db.models
        draw_grapt(self.genv)
        file_data = open('genv_to_image.png',"rb")
        data = file_data.read()
        fs = gridfs.GridFS(db)
        id = fs.put(data, filename=self.id)
        models.insert_one({
            "population": 1,
            "name": self.id,
            "genv": self.genv,
            "genv_to_images": id,
            "loss_train": self.loss_train,
            "loss_test": self.loss_test,
            "acc": self.acc
        })
