import random
import numpy as np
from config import BLOCK_SIZE, W, H, N_STATE, N_ACTION, PINK
from environment import Point
state_to_index = lambda x:int(''.join(str(v) for v in list(x)),2)  
def index_to_state(x):
    x = format(int(x), 'b').zfill(N_STATE)
    state = []
    for i in x: 
        state.append(int(i))
    return np.array(state) 
# q_table = np.random.uniform(low=-2, high=0, size=(n_state, n_action))
class Agent:
    def __init__(self, env,id,en = 100):
        self.en = en
        self.env = env
        self.id = id
        self.c_learning_rate = 0.1 # randomness
        self.c_discount_value = 0.9
        self.death = False
        self.branin = np.random.uniform(low=-1, high=1, size=(N_STATE, N_ACTION))
        self.color = (255,255,255)
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
    def get_state(self, action=[0]*5):
        state = self.env.get_state_agent(self.id, action)
        return np.array(state, dtype=int)
    def get_action(self,state):
        final_move = [0]*5
        if random.randint(0,2) < self.env.days:
            index = random.randint(0, 4)
        else:
            state = state_to_index(state)
            index = np.argmax(self.branin[state])
        final_move[index] = 1
        return final_move
    def take_action(self,state):
        action = self.get_action(state)
        x = self.pos.x
        y = self.pos.y
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
        if x < 0:
            x = 0
        elif x > W - BLOCK_SIZE:
            x = W - BLOCK_SIZE
        if y < 0:
            y = 0
        elif y > H - BLOCK_SIZE:
            y = y - BLOCK_SIZE
        self.pos = Point(x,y)
        en,death = self.env.set_agent(self.id)
        self.en +=en
        reward = en 
        self.death = death
        state_new = self.get_state(action)
        # check death
        if(self.en < 0):
            self.death = True
            self.env.set_death(self.id)
            return action, reward, state_new
        return action, reward, state_new
    def add_children(self):
        # print('asfdsdf')
        children = type(self)(self.env, len(self.env.population))
        children.set_pos(self.pos)
        children.branin =self.branin.copy()
        children.color = PINK
        self.env.add_agent(children)
    def train(self, state_old, action, reward, state_new):
        index = state_to_index(state_old)
        current_q_value = self.branin[index][np.argmax(action)]
        new_q_value = (1 - self.c_learning_rate) * current_q_value + self.c_learning_rate * (reward + self.c_discount_value * np.max(self.branin[state_to_index(state_new)]))
        self.branin[index][np.argmax(action)] = new_q_value
    def run(self):
        is_children = False
        Q_T = []
        if self.death == False:
            # print("Id: ", self.id, " En: ", self.en)
            state_old = self.get_state()
            action, reward, state_new = self.take_action(state_old)
            if self.en < -300:
                self.en -=100
                is_children = True
                self.add_children()
                Q_T = self.branin.copy()
            self.train(state_old, action, reward, state_new)
            return is_children, Q_T, self.pos
        return False, [], self.pos