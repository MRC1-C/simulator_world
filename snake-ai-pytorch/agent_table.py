import torch
import random
import numpy as np
from collections import deque
from game import SnakeGameAI, Direction, Point
from model import Linear_QNet, QTrainer
from helper import plot

MAX_MEMORY = 100_000
BATCH_SIZE = 1000
LR = 0.001
state_to_index = lambda x:int(''.join(str(v) for v in list(x)),2)  
def index_to_state(x):
    x = format(int(x), 'b').zfill(n_state)
    state = []
    for i in x: 
        state.append(int(i))
    return np.array(state) 
n_state = 2047
n_action = 3
q_table = np.random.uniform(low=-2, high=0, size=(n_state, n_action))



class Agent:

    def __init__(self):
        self.n_games = 0
        self.c_learning_rate = 0.1 # randomness
        self.c_discount_value = 0.9
        self.Q_table = np.random.uniform(low=-1, high=1, size=(n_state, n_action))


    def get_state(self, game):
        head = game.snake[0]
        body = game.snake[1:]
        point_l = Point(head.x - 20, head.y)
        point_r = Point(head.x + 20, head.y)
        point_u = Point(head.x, head.y - 20)
        point_d = Point(head.x, head.y + 20)
        
        dir_l = game.direction == Direction.LEFT
        dir_r = game.direction == Direction.RIGHT
        dir_u = game.direction == Direction.UP
        dir_d = game.direction == Direction.DOWN

        state = [
            # Danger straight
            (dir_r and (point_r in body or game.is_collision(point_r))) or 
            (dir_l and (point_l in body or game.is_collision(point_l))) or 
            (dir_u and (point_u in body or game.is_collision(point_u))) or 
            (dir_d and (point_d in body or game.is_collision(point_d))),

            # Danger right
            (dir_u and (point_r in body or game.is_collision(point_r))) or 
            (dir_d and (point_l in body or game.is_collision(point_l))) or 
            (dir_r and (point_d in body or game.is_collision(point_d))),

            # Danger left
            (dir_d and (point_r in body or game.is_collision(point_r))) or 
            (dir_u and (point_l in body or game.is_collision(point_l))) or 
            (dir_l and (point_d in body or game.is_collision(point_d))),
            
            # Move direction
            dir_l,
            dir_r,
            dir_u,
            dir_d,
            
            # Food location 
            game.food.x < game.head.x,  # food left
            game.food.x > game.head.x,  # food right
            game.food.y < game.head.y,  # food up
            game.food.y > game.head.y  # food down
            ]

        return np.array(state, dtype=int)

    def train_short_memory(self, state, action, reward, next_state, done):
        index = state_to_index(state)
        current_q_value = self.Q_table[index][np.argmax(action)]
        new_q_value = (1 - self.c_learning_rate) * current_q_value + self.c_learning_rate * (reward + self.c_discount_value * np.max(self.Q_table[state_to_index(next_state)]))
        self.Q_table[index][np.argmax(action)] = new_q_value
    def get_action(self, state):
        # random moves: tradeoff exploration / exploitation
        state = state_to_index(state)
        index = np.argmax(self.Q_table[state])
        if index == 0:
            return np.array([1,0,0])
        elif index == 1:
            return np.array([0,1,0])
        else: 
            return np.array([0,0,1]) 


def train():
    plot_scores = []
    plot_mean_scores = []
    total_score = 0
    record = 0
    agent = Agent()
    game = SnakeGameAI()
    while True:
        # get old state
        state_old = agent.get_state(game)

        # get move
        final_move = agent.get_action(state_old)

        # perform move and get new state
        reward, done, score = game.play_step(final_move)
        state_new = agent.get_state(game)

        # train short memory
        agent.train_short_memory(state_old, final_move, reward, state_new, done)

        # remember
        if done:
            # train long memory, plot result
            game.reset()
            agent.n_games += 1
            # agent.train_long_memory()

            if score > record:
                record = score

            print('Game', agent.n_games, 'Score', score, 'Record:', record)

            plot_scores.append(score)
            total_score += score
            mean_score = total_score / agent.n_games
            plot_mean_scores.append(mean_score)
            plot(plot_scores, plot_mean_scores)


if __name__ == '__main__':
    train()