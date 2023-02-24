import pygame
from timer import DelayTime
from setting import *

class UI:
    def __init__(self, population_sprites) -> None:
        self.dislay_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, FONT_SIZE)
        self.fps = 0
        self.energy = 100
        self.population_sprites = population_sprites
        self.quantity = len(population_sprites) 
        self.timer = {
            "fps": DelayTime(1000),
            "energy": DelayTime(1000),
            "quantity": DelayTime(1000),
        }
    def show_fps(self,dt):
        if self.timer['fps'].active:
            self.fps = int(1/dt)
        text_surf = self.font.render(f"FPS: {self.fps}",False, FONT_COLOR)
        text_rect = text_surf.get_rect(topright = FPS_POS)
        self.dislay_surface.blit(text_surf, text_rect)

    def show_energy(self):
        if self.timer['energy'].active:
            for sprite in self.population_sprites: 
                self.energy = int(sprite.energy)
        t = self.font.render(f"ENERGY: {self.energy}",False, FONT_COLOR)
        t_r = t.get_rect(topleft = (4,0))
        self.dislay_surface.blit(t, t_r)

    def show_quantity(self):
        if self.timer['quantity'].active:
            self.quantity = len(self.population_sprites)
        t = self.font.render(f"Quantity: {self.quantity}",False, FONT_COLOR)
        t_r = t.get_rect(topleft = (4,0))
        self.dislay_surface.blit(t, t_r)

    def update_timer(self):
        for timer in self.timer.values():
            timer.update()

    def display(self,dt):
        self.update_timer()
        self.show_fps(dt)
        self.show_quantity()
        # self.show_energy()

