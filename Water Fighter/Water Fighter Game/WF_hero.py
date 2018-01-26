import pygame, sys
from pygame.locals import *
from WF_weapons import *
pygame.init()
  
    
class Hero(pygame.sprite.Sprite):
  def __init__(self, counter):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load("Images/Character/pika.png")
    self.rect = self.image.get_rect()
    self.rect.midbottom = (50,420)
    
    self.vel_x = 0 
    self.vel_y = 0
    self.accel = 0.5
    
    self.jump = False
    self.collide = False
    self.counter = counter

    self.weapons = Weapons(counter)
    
    #Determines direction of character#
    self.dirx = 1
    

  def accel_left(self):
    self.vel_x = -4
    self.dirx = -1

  def accel_right(self):
    self.vel_x = 4
    self.dirx = 1

  def accel_up(self):
    if not self.jump:
      self.vel_y = -18
      self.jump = True
      self.collide = False
       
  def control(self, keys):
    if keys[K_LEFT] and keys[K_RIGHT]:
      self.vel_x = 0 
      
    elif keys[K_LEFT]:
      self.accel_left()
     
    elif keys[K_RIGHT]:
      self.accel_right()

    if keys[K_SPACE]:
      self.accel_up()
      
    if keys[K_LCTRL]:
      self.fire()
     
  def fire(self):
    self.weapons.build(self.rect.center, self.dirx)
    
  def check(self):
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
      
      
  def update(self, keys):
    self.control(keys)
    self.check()
    
