import pygame
import sys
from setting import *
from level import Level

class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("SW")
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.clock = pygame.time.Clock()
        self.level = Level()
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            dt = self.clock.tick()/1000
            self.level.run(dt)
            pygame.display.update()
if __name__ == '__main__':
    game = Game()
    game.run()