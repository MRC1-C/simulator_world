import pygame
import random
from config import WHITE,RED,BLUE1,BLACK,W,H,N_FOOD,N_TIME,N_DAYS,BLOCK_SIZE ,SPEED, Point
from agent_deep import Agent_D
from helper import plot
import copy
# pygame = pygame
# print(type(copy.copy(pygame)))
pygame.init()
font = pygame.font.Font('arial.ttf', 25)

class Environmaent:
    def __init__(self,name, w=W, h=H, n_food = N_FOOD, n_time = N_TIME, n_days = N_DAYS):
        self.w = w
        self.h = h
        self.n_food = n_food
        self.n_time = n_time
        self.name = name
        # self.plot = None
        self.population = []
        self.days = 0
        self.n_days = n_days
        # init display
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('Protozoan')
        self.clock = pygame.time.Clock()
        self.reset()

    def add_agent(self,agent):
        self.population.append(agent)
        # print(self.population)
    def set_agent(self, id):
        death = False
        en = -1
        pos = self.population[id].pos
        for f in self.food:
            if pos == f:
                en = 40
                self.food.remove(f)
        return en, death
    def set_death(self,id):
        self.population[id] = None
    def reset(self):
        self.food = []
        self._place_food()
        self.time = 0

    def get_state_agent_test(self, id, memory, n):
        pos_agent = self.population[id].pos
        pos_x = pos_agent.x
        pos_y = pos_agent.y
        state = [0]*24
        k = 0 
        for i in range(-n,n+1):
            for j in range(-n,n+1):
                if (i,j) != (0,0):
                    point = Point(pos_x+i*BLOCK_SIZE, pos_y+j*BLOCK_SIZE)
                    if point in self.food:
                        state[k] = 1
                    k+=1
        # print(state)
        return state + list(memory)
                    
    def get_state_agent(self, id, memory):
        pos_agent = self.population[id].pos
        pos_x = pos_agent.x
        pos_y = pos_agent.y
        state = [0]*8
        pos = []
        up_pos = Point(pos_x,pos_y+BLOCK_SIZE)
        pos.append(up_pos)
        down_pos = Point(pos_x,pos_y-BLOCK_SIZE)
        pos.append(down_pos)
        left_pos = Point(pos_x-BLOCK_SIZE,pos_y)
        pos.append(left_pos)
        right_pos = Point(pos_x+BLOCK_SIZE,pos_y)
        pos.append(right_pos)
        up_right_pos = Point(pos_x+BLOCK_SIZE,pos_y+BLOCK_SIZE)
        pos.append(up_right_pos)
        up_left_pos = Point(pos_x-BLOCK_SIZE,pos_y+BLOCK_SIZE)
        pos.append(up_left_pos)
        down_right_pos = Point(pos_x+BLOCK_SIZE,pos_y-BLOCK_SIZE)
        pos.append(down_right_pos)
        down_left_pos = Point(pos_x-BLOCK_SIZE,pos_y-BLOCK_SIZE)
        pos.append(down_left_pos)
        for index, p in enumerate(pos):
            if p in self.food:
                state[index] = 1
        # print(action)
        return state + list(memory)

    def _place_food(self):
        self.food = []
        for _ in range(self.n_food):
            x = random.randint(0, (self.w-BLOCK_SIZE )//BLOCK_SIZE )*BLOCK_SIZE
            y = random.randint(0, (self.h-BLOCK_SIZE )//BLOCK_SIZE )*BLOCK_SIZE
            self.food.append(Point(x, y))

    def stop(self):
        pygame.quit()

    def run(self):
        # print("N: {}/{}".format(sum(x is not None for x in self.population), len(self.population)))
        self.time += 1
        is_new_day = False
        # 1. collect user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #check stop
        stop = False
        if (self.days > self.n_days and set(self.population) == {None}) or not self.food:
            stop = True
            for i in self.plot:
                i.append(0)
            plot(self.plot, self.name)
        # 3. check new day
        if self.time == self.n_time:
            if self.days ==0:
                self.plot = []
                for _ in range(len(self.population)):
                    arr = []
                    self.plot.append(arr.copy())
            for i in range(len(self.population)):
                if self.population[i]:
                    self.plot[i].append(self.population[i].en) 
                else:
                    self.plot[i].append(0)
            self.time = 0
            self.days +=1
            is_new_day = True
        self._update_ui()
        self.clock.tick(SPEED)
        for agent in self.population:
            if agent:
                agent.run()
        return stop,sum(x is not None for x in self.population),len(self.population),is_new_day


    def _update_ui(self):
        self.display.fill(BLACK)
        for food in self.food:
            pygame.draw.rect(self.display, RED, pygame.Rect(food.x, food.y, BLOCK_SIZE, BLOCK_SIZE))
        for agent in self.population:
            if agent:
                pos = agent.pos
                pygame.draw.rect(self.display, agent.color, pygame.Rect(pos.x, pos.y, BLOCK_SIZE, BLOCK_SIZE))
        text = font.render("Days: " + str(self.days) + " Time: " + str(self.time) + " N: {}/{}".format(sum(x is not None for x in self.population), len(self.population)), True, WHITE)
        self.display.blit(text, [0, 0])
        pygame.display.flip()

