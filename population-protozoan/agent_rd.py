import random
import numpy as np
from config import BLOCK_SIZE, W, H, Point
# from environment import Environmaent
from collections import deque
import torch
from model import Linear_QNet, QTrainer
from copy import deepcopy
MAX_MEMORY = 3
BATCH_SIZE = 3
LR = 0.001

class Agent_RD:
    def __init__(self, env,id,en = 100):
        self.en = en
        self.env = env
        self.id = id
        self.death = False
        self.gamma = 0.9
        self.memory = deque(maxlen=MAX_MEMORY) 
        self.branin = Linear_QNet(21, 256, 5)
        self.trainer = QTrainer(self.branin, lr=LR, gamma=self.gamma)
        self.color = "blue"
        self.reset() 
    def set_pos(self,pos):
        x = pos.x + BLOCK_SIZE
        y = pos.y
        self.pos = Point(x,y)
    def reset(self):
        self.pos = None
        x = random.randint(0, (W-BLOCK_SIZE )//BLOCK_SIZE )*BLOCK_SIZE
        y = random.randint(0, (H-BLOCK_SIZE )//BLOCK_SIZE )*BLOCK_SIZE
        self.pos = Point(x,y)
    def get_state(self, action=[0]*13):
        state = self.env.get_state_agent(self.id, action)
        return np.array(state, dtype=int)
    def remember(self, state, action, reward, next_state):
        self.memory.append((state, action, reward, next_state))

    def train_long_memory(self):
        if len(self.memory) > BATCH_SIZE:
            mini_sample = random.sample(self.memory, BATCH_SIZE)
        else:
            mini_sample = self.memory
        states, actions, rewards, next_states = zip(*mini_sample)
        self.trainer.train_step(states, actions, rewards, next_states)
        for state, action, reward, next_state, done in mini_sample:
           self.trainer.train_step(state, action, reward, next_state, done)
    def train(self, state, action, reward, next_state):
        self.trainer.train_step(state, action, reward, next_state)
    def get_action(self,state):
        final_move = [0]*5
        move = random.randint(0, 4)
        final_move[move] = 1
        # if random.randint(0, 2) < self.env.days:
        #     move = random.randint(0, 4)
        #     final_move[move] = 1
        # else:
        #     state0 = torch.tensor(state, dtype=torch.float)
        #     prediction = self.branin(state0)
        #     move = torch.argmax(prediction).item()
        #     final_move[move] = 1

        return final_move
    def add_children(self):
        children = type(self)(self.env, len(self.env.population))
        children.set_pos(self.pos)
        children.color = (100,100,100)
        children.branin = deepcopy(self.branin) 
        self.env.add_agent(children)
    def take_action(self,state):
        action = self.get_action(state)
        x = self.pos.x
        y = self.pos.y
        en_ = 0
        if np.array_equal(action, [1,0,0,0,0]):
            x += BLOCK_SIZE
        elif np.array_equal(action, [0,1,0,0,0]):
            x -= BLOCK_SIZE
        elif np.array_equal(action, [0,0,1,0,0]):
            y += BLOCK_SIZE
        elif np.array_equal(action, [0,0,0,1,0]):
            y -= BLOCK_SIZE
        elif np.array_equal(action, [0,0,0,0,1]):
            self.pos = self.pos
            en_ = 0.4
        if x < 0:
            x = 0
            en_ = -5
        elif x > W - BLOCK_SIZE:
            x = W - BLOCK_SIZE
            en_ = -5
        if y < 0:
            y = 0
            en_ = -5
        elif y > H - BLOCK_SIZE:
            y = y - BLOCK_SIZE
            en_ = -5
        self.pos = Point(x,y)
        en,death = self.env.set_agent(self.id)
        en +=en_
        self.en +=en
        reward = 0
        if en > 9:
            reward =10
        else:
            reward = en
            # self.en-=1
        # print(reward)
        self.death = death
        state_new = self.get_state(action+list(state[:8]))
        # check death
        if(self.en < 0):
            self.death = True
            self.env.set_death(self.id)
            return action, reward, state_new
        return action, reward, state_new
    def run(self):
        is_children = False
        branin = []
        if self.death == False:
            # print("Id: ", self.id, " En: ", self.en)
            state_old = self.get_state()
            action, reward, state_new = self.take_action(state_old)
            if self.en < -300:
                self.en -=100
                self.add_children()
                branin =self.branin
            self.train(state_old, action, reward, state_new)
            # self.remember(state_old, action, reward, state_new)
            return is_children, branin, self.pos
        return False, [], self.pos
