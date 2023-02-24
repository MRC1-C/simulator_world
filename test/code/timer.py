import pygame

class Timer:
    def __init__(self, duraction = 100, func = None) -> None:
        self.duration = duraction
        self.func = func
        self.start_time = 0
        self.active = False
    def activate(self):
        self.active = True
        self.start_time = pygame.time.get_ticks()
    
    def deactivate(self):
        self.active = False

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.start_time >= self.duration:
            self.deactivate()
            if self.func:
                self.func()

class DelayTime:
    def __init__(self, duraction = 100, func = None) -> None:
        self.duration = duraction
        self.start_time = 0
        self.active = True

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.start_time >= self.duration:
            self.active = True
            self.start_time = pygame.time.get_ticks()
        else: 
            self.active = False