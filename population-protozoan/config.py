from collections import namedtuple
WHITE = (255, 255, 255)
RED = (200,0,0)
BLUE1 = (0, 0, 255)
BLUE2 = (0, 100, 255)
PINK = (124,252,0)
BLACK = (0,0,0)
W = 640
H = 640
N_TIME = 100
N_DAYS = 2
BLOCK_SIZE = 4
SPEED = 80
LR = 0.001
N_STATE = 8191
N_ACTION = 5
N_FOOD = 5000
N_POPULATION = 5
SENSE = 2
Point = namedtuple('Point', 'x, y')