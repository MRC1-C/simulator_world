import pygame
from sprites import Generic, Individual
from setting import *
from ui import UI
import random

class Level:
    def __init__(self) -> None:

        self.display_surface = pygame.display.get_surface()
        self.camera = Camera()
        self.obstacle_sprites = pygame.sprite.Group()
        self.population_sprites = pygame.sprite.Group()
        self.food_sprites = pygame.sprite.Group()
        self.ui = UI(self.population_sprites)

        self.setup()
    
    def setup(self):
        food = pygame.image.load("../graphics/grass/grass_2.png").convert_alpha()
        food = pygame.transform.scale(food,(TITLE_SIZE,TITLE_SIZE))
        
        o = pygame.image.load("../graphics/objects/10.png").convert_alpha()
        o = pygame.transform.scale(o,(TITLE_SIZE,TITLE_SIZE))

        for i in range(0,len(WORLD_MAP)):
            for j in range(0,len(WORLD_MAP)):
                if i == 0 or j == 0 or i == len(WORLD_MAP)-1 or j == len(WORLD_MAP)-1:
                    Generic((i*TITLE_SIZE,j*TITLE_SIZE), [self.obstacle_sprites,self.camera],o)    
                else:
                    if random.random() < 0.1:
                        Generic((i*TITLE_SIZE,j*TITLE_SIZE), [self.food_sprites,self.camera],food)
        for i in range(1,2):          
            Individual((i*10*30,10*30),[self.camera,self.population_sprites],self.obstacle_sprites,self.population_sprites, self.food_sprites)
    def run(self,dt):
        self.camera.custom_draw()
        self.camera.update(dt)
        self.ui.display(dt)

class Camera(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()
        self.zoom = 1

    def event(self):
        mouse = pygame.mouse.get_pressed()
        if mouse[0]:
            pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_HAND))
            m = pygame.mouse.get_rel()
            if abs(m[0]) < 50 and abs(m[1]) < 50:
                self.offset -= m
        elif not(mouse[0] and mouse[1] and mouse[2]):
            pygame.mouse.set_cursor(0)

        key = pygame.key.get_pressed()
        if key[pygame.K_q]:
            self.zoom +=0.1
        if key[pygame.K_w]:
            self.zoom -=0.1
            if self.zoom <=1:
                self.zoom = 1
    def custom_draw(self):
        self.event()
        # internal_surf = pygame.Surface((WIDTH,HEIGHT))
        # internal_surf.fill("lightblue")
        self.display_surface.fill("lightblue")
        for sprite in self.sprites():
            offset_rect = sprite.rect.copy()
            offset_rect.center -= self.offset
            self.display_surface.blit(sprite.image, offset_rect)
            # internal_surf.blit(sprite.image, offset_rect)
        # scaled_surf = pygame.transform.rotozoom(internal_surf,0,self.zoom)
        # scaled_rect = scaled_surf.get_rect(center = (WIDTH/2,HEIGHT/2))
        # self.display_surface.blit(scaled_surf,scaled_rect)