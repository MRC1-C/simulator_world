import pygame
from setting import *
import random
from support import import_folder
from Q_learning import CNN
import torch

class Generic(pygame.sprite.Sprite):
	def __init__(self, pos, groups, surf = pygame.Surface((TITLE_SIZE,TITLE_SIZE))):
		super().__init__(groups)
		self.image = surf
		self.rect = self.image.get_rect(topleft = pos)

class Individual(pygame.sprite.Sprite):
	def __init__(self, pos, groups,obstacle_sprites,population_sprites,food_sprites,size = TITLE_SIZE) -> None:
		super().__init__(groups)
		# self.d = pygame.display.get_surface()
		self.obstacle_sprites = obstacle_sprites
		self.population_sprites = population_sprites
		self.food_sprites = food_sprites
		self.scale = 10
		self.size = size
		self.energy = 100
		self.reward = 0
		self.image = pygame.Surface((size*self.scale,size*self.scale),pygame.SRCALPHA)
		pygame.draw.polygon(self.image, pygame.Color(255, 255, 255, 128), ((self.image.get_width()/2,self.image.get_width()/2-10), (0,0), (self.image.get_width(),0)))
		
		self.dt = 0
		#model
		self.cnn = CNN()

		#animation
		self.import_graphics(size)
		self.frame_index = 0
		self.c = self.animation[self.frame_index]
		self.c_rect = self.c.get_rect(center = (size*self.scale/2,size*self.scale/2))
		
		
		self.image.blit(self.c,self.c_rect)
		self.original_image = self.image
		self.position = pygame.math.Vector2(pos)	
		self.direction = pygame.math.Vector2(0, -1)
		self.max_speed = 200
		self.speed = 0
		self.angle_speed = 0
		self.angle = random.randint(0,360)
		self.rect = self.image.get_rect(center=pos)
		self.hitbox = self.rect.inflate(-size*(self.scale-1),-size*(self.scale-1))
		self.mouth = self.hitbox.inflate(-self.size/2,-self.size/2)
		self.mouth.center = self.rect.center
		if self.angle !=0:
			self.direction.rotate_ip(self.angle)
			self.image = pygame.transform.rotate(self.original_image, -self.angle)
	
	def input(self,dt):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_UP]:
			if self.speed + 1 <= self.max_speed:
				self.speed +=1
		elif keys[pygame.K_DOWN]:
			if self.speed - 1 >= 0:
				self.speed -=1
		else:
			self.speed = self.speed
		if keys[pygame.K_LEFT]:
			self.angle_speed = -0.5
		elif keys[pygame.K_RIGHT]:
			self.angle_speed = 0.5
		else:
			self.angle_speed = 0
		self.energy -= dt*self.speed*0.01

		self.animate(dt)
		self.direction.rotate_ip(self.angle_speed*dt*1000)
		self.angle += self.angle_speed*dt*1000
		self.image = pygame.transform.rotate(self.original_image, -self.angle)
		self.rect = self.image.get_rect(center=self.hitbox.center)
		self.position += self.direction * self.speed * dt
		self.hitbox.center = self.position
		self.rect.center = self.position
	
	def animate(self):
		self.frame_index += 5*self.dt
		if self.frame_index >= len(self.animation):
			self.frame_index = 0
		if self.speed == 0:
			self.frame_index = 0
		self.image = pygame.Surface((self.size*self.scale,self.size*self.scale),pygame.SRCALPHA)
		pygame.draw.polygon(self.image, pygame.Color(255, 255, 255, 128), ((self.image.get_width()/2,self.image.get_width()/2-10), (0,0), (self.image.get_width(),0)))
		
		self.c = self.animation[int(self.frame_index)]
		self.c = pygame.transform.scale(self.c,(self.size,self.size))
		self.c_rect = self.c.get_rect(center = (self.size*self.scale/2,self.size*self.scale/2))
		self.image.blit(self.c,self.c_rect)
		self.original_image = self.image
		# self.hitbox = self.rect.inflate(-self.size*(self.scale-1),-self.size*(self.scale-1))
		self.angle += self.angle_speed*self.dt*1000
		if self.angle != 0:
			self.direction.rotate_ip(self.angle_speed*self.dt*1000)
			self.image = pygame.transform.rotate(self.original_image, -self.angle)
		self.rect = self.image.get_rect()
		self.position += self.direction * self.speed * self.dt
		self.hitbox.center = self.position
		self.mouth.center = self.position
		self.rect.center = self.position

	def import_graphics(self,size,name="character"):
		self.animation = []
		path = f"../graphics/{name}"
		self.animation = import_folder(size,path)

	def move(self):
		# input = torch.randn(1,4,4)
		# output = self.cnn(input)[0].detach().numpy()
		# action = [round(output[0]),round(output[1])] 
		action = [random.randint(-1,1),random.randint(-1,1)]
		if action[0] == 0:
			self.speed -=0
		elif action[0] == 1:
			if self.speed + 10 <= self.max_speed:
				self.speed +=10
		else:
			if self.speed - 10 >= -self.max_speed:
				self.speed -= 10
		if action[1] == 0:
			self.angle_speed =0
		elif action[1] == 1:
			self.angle_speed =0.5
		else:
			self.angle_speed =-0.5
		self.energy -= self.dt*self.speed*0.01
	
	def collision(self):
		for sprite in self.obstacle_sprites:
			if sprite.rect.colliderect(self.hitbox):
				self.position -= 1.2*self.direction * self.speed * self.dt
				self.hitbox.center = self.position
				self.rect.center = self.position
				self.speed = 0
		for sprite in self.food_sprites:	
				if self.speed > 0:
					if sprite.rect.colliderect(self.mouth):
						sprite.kill()
						self.energy +=30
						f = 0.1*self.energy/100
						if self.size <= TITLE_SIZE*1.5:
							self.size = self.size+f
						self.hitbox.width = self.size
						self.hitbox.height = self.size
						# self.mouth = self.hitbox.inflate(-self.size/2,-self.size/2)
						self.mouth.width = self.size/2
						self.mouth.height = self.size/2
						# self.mouth.center = self.rect.center
				else:
					if sprite.rect.colliderect(self.hitbox):
						self.position -= 1.2*self.direction * self.speed * self.dt
						self.hitbox.center = self.position
						self.rect.center = self.position
						self.speed = 0
		for sprite in self.population_sprites:
			if self.hitbox.center != sprite.hitbox.center:
				if self.hitbox.colliderect(sprite.hitbox):
					self.speed = 0
					# sprite.kill()
		
	def check_death(self):
		if self.energy < 0:
			self.kill()

	def get_status(self):
		# mask = pygame.Surface((self.size*self.scale,self.size*self.scale))
		# mask.fill('black')
		t = self.d.subsurface(self.rect)
		pygame.draw.polygon(t, "red", ((t.get_width()/2,t.get_width()/2-10), (0,0), (t.get_width(),0)))
		# t.blit(mask,(0,0))
		pygame.image.save(t,f"test/{int(pygame.time.get_ticks())}_.png")
	def update(self,dt):
		self.dt = dt
		# self.input()
		self.move()
		self.animate()
		self.collision()
		self.check_death()
		# self.get_status()
		# self.k = self.hitbox.inflate(-self.size/2,-self.size/2)
		# p = pygame.Surface((self.k.width,self.k.height))
		# p_r = p.get_rect(center = self.rect.center)
		# self.d.blit(p,p_r)
		# o = pygame.Surface((self.hitbox.width,self.hitbox.height))
		# o.fill('red')
		# self.d.blit(o,self.hitbox)
		# self.f = self.display_surface.subsurface((self.rect.x,self.rect.y),(self.rect.width,self.rect.height))
		# pygame.image.save(self.f,f"test/test{int(pygame.time.get_ticks())}.png")
