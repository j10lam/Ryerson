import pygame, sys
from pygame.locals import *
from WF_weapons import *
pygame.init()
  
    
class Hero(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load("pika.png")
    self.rect = self.image.get_rect()
    self.rect.center = (100,0)
    
    self.angle = 20
    self.rotate = 0 
    
    self.vel_x = 0 
    self.vel_y = 0
    self.accel = 0.5
    self.jump = False
    self.collide = False
    
  def accel_left(self):
    self.vel_x = -5

  def accel_right(self):
    self.vel_x = 5
  
  def accel_up(self):
    self.vel_y = -18
       
  def control(self, keys, weapons, timer):
    if not self.jump:
      if keys[K_a] and keys[K_d]:
        self.vel_x = 0 
        
      elif keys[K_a]:
        self.accel_left()
       
      elif keys[K_d]:
        self.accel_right()
  
      if keys[K_SPACE]:
        self.accel_up()
        self.jump = True
        self.collide = False
     
    weapons.build(keys, self.rect.center, self.angle, timer, self.rotate)
    
  def update(self):
    
    self.rect.centerx += self.vel_x
    self.rect.centery += self.vel_y
    
     # in mid air #
    if not self.collide:
      self.vel_y += self.accel
      
    # Landing #
    elif self.collide:
      self.jump = False
      self.vel_y = 0
      
    # Stop moving automatically #            
    if not self.jump:
      self.vel_x = 0
       
class Hero_control(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.hero = Hero()
    self.tank = Tank()
    self.jet = Jetpack()
    self.checks = [True, False, False]
    
    self.weapons = Weapons()
    self.char = pygame.sprite.GroupSingle()
    
  def check(self):
    if self.checks[0]:
      self.char.add(self.hero)
    elif self.checks[1]:
      self.char.add(self.tank)
    elif self.checks[2]:
      self.char.add(self.jet)
        
  def control(self, keys, timer):
    if self.checks[0]:
      self.hero.control(keys, self.weapons, timer)
    elif self.checks[1]:
      self.tank.control(keys, self.weapons, timer)
    elif self.checks[2]:
      self.jet.control(keys, self.weapons, timer)
      
  def update(self, keys, timer):
    self.check()
    self.control(keys, timer)
            