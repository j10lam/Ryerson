import pygame, math, random
from WF_animation import *


class Bullet(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.animate = Animation(28, 28, "Images/Weapons/waterballoon.png")
    self.image = self.animate.frame_images_normal[0]
    self.rect = self.image.get_rect()
    self.rect.size = (15,15)
    self.dirx = 1
    self.dmg = 2     
    self.hit = False
    
  def update(self):
    self.rect.centerx += 6* self.dirx
    
    #Animation#
    self.image = self.animate.frame_images_normal[self.animate.frame]
    self.image = pygame.transform.scale(self.image, (15,15))
    self.animate.frame_update(self.hit)

class Water(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.animate = Animation(28, 28, "Images/Weapons/waterballoon.png")
    self.image = self.animate.frame_images_normal[0]
    self.rect = self.image.get_rect()
    
    self.dx, self.dy = (0, 0)
    self.speed = 15
    self.accel = 0.5
    self.angle = 20
    self.dirx = 1
    self.dmg = 10
    self.hit = False
   
  def calcvector(self):
    #Calculates initial vector#
    radians = self.angle * math.pi/180
   
    self.dx = self.speed * math.cos(radians)
    self.dy = self.speed * math.sin(radians)
    self.dy *= -1
    self.dx *= self.dirx
    
  def update(self):
    #Updates the waterballoon#
    self.dy += self.accel
    self.rect.centerx += self.dx
    self.rect.centery += self.dy       
    
    if not self.hit:    
      self.image = self.animate.frame_images_normal[self.animate.frame]
      
    elif self.hit:
      self.image = self.animate.frame_images_killed[self.animate.frame_killed]
      
    self.animate.frame_update(self.hit)
  
class Rocket(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    
    #Initial Animation call, creates the animation lists#
    self.animate = Animation(49, 21, "Images/Weapons/rocket.png")
    self.image = self.animate.frame_images_normal[0]
    self.rect = self.image.get_rect()
    
    self.vel_x = 0 
    self.accel = 0.5
    self.dirx = 1
    self.dmg = 10 
    self.hit = False
    
  def update(self):
   #If not hit does the following:#
    if not self.hit:    
      self.vel_x += self.accel
      self.rect.centerx += self.vel_x * self.dirx
      if self.dirx == 1:
        self.image = self.animate.frame_images_normal[self.animate.frame]
      elif self.dirx == -1:
        self.image = self.animate.frame_images_r_normal[self.animate.frame]
        
    #If hit does the following:#
    if self.hit:
      if self.dirx == 1:
        self.image = self.animate.frame_images_killed[self.animate.frame_killed]
      elif self.dirx == -1:
        self.image = self.animate.frame_images_r_killed[self.animate.frame_killed]
              
    #Updates the frames#
    self.animate.frame_update(self.hit)
    
    
class Weapons(pygame.sprite.Sprite):
  def __init__(self, counter):
    pygame.sprite.Sprite.__init__(self)
    
    #Weapon group container#
    self.weapons = pygame.sprite.Group()
    self.weapons2 = pygame.sprite.Group() #Handles sprites that explode#
        
    #Flags to switch certain weapons on/off#
    self.weapons_list = [True, False, False, False]
    self.counter = counter
    
  def build(self, pos, dirx):

    #Checks for a flag in the list: self.weapons that is True#
    if self.weapons_list[0]:
      #A timer to restrict the amount of objects created at one time#
      if self.counter.bullet_wait <1:
        #Creates an object#
        bullet = Bullet()
        
        #Giving the object attributes#
        bullet.rect.center = pos
        bullet.dirx = dirx
        
        #Adding the object to the group#
        self.weapons.add(bullet)
        
        #Increases the wait time#
        self.counter.bullet_wait += self.counter.bullet_delay
        
    elif self.weapons_list[1]:  
      if self.counter.special_wait <1:
        balloon = Water()
        balloon.rect.center = pos
        balloon.dirx = dirx
        
        balloon.calcvector() 
        
        self.weapons2.add(balloon)
        self.counter.special_wait += self.counter.special_delay
    
    elif self.weapons_list[2]:
      if self.counter.bullet_wait <1:
        #A bullet traveling left#
        bullet_left = Bullet()
        bullet_left.rect.center = pos
        bullet_left.dirx = -1      
        
        #A bullet traveling right#
        bullet_right = Bullet()
        bullet_right.rect.center = pos

        self.weapons.add(bullet_left, bullet_right)
        self.counter.bullet_wait += self.counter.bullet_delay
        
    elif self.weapons_list[3]:
      if self.counter.special_wait <1:
        rocket = Rocket()
        rocket.rect.center = pos  
        rocket.dirx = dirx

        self.weapons2.add(rocket)
        self.counter.special_wait += self.counter.special_delay
                  
  def reset(self):
    #Rests all flags in self.weapons to False#
    for weapon in range(len(self.weapons_list)):
      self.weapons_list[weapon] = False
         


