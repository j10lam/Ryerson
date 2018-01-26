import pygame, sys, random
from pygame.locals import *
from WF_animation import *
pygame.init()

class Enemy(pygame.sprite.Sprite):
  def __init__(self, filename, frame_width, frame_height, damage, pos, speed, hp, points):
    pygame.sprite.Sprite.__init__(self)  
    
    #Creates the animation lists for the Enemy class for each enemy sprite#
    self.animate = Animation(frame_width, frame_height, filename)  
    
    '''Enemy sprite's initial characteristics'''
    #Assigns the first frame as the initial image#
    self.image = self.animate.frame_images_normal[0]
    self.rect = self.image.get_rect()
    self.rect.center = pos
    self.hp = hp
    self.points = points
    
    #Self.killed determined animations#
    self.killed = False
    self.damaged = False
    self.dirx = 1
    
    #Special attributes for each type of enemy#
    self.dmg = damage
    self.speed = speed
    
  def hit(self, wep_dmg, points):
    #Decreases enemy hp#
    self.hp -= wep_dmg
    if self.hp <= 0:           
      self.killed = True
      
      #If not initially hit, update kills#
      if not self.damaged:
        points.kills_update()
        #Changes to True, so that kill will only update once#
        self.damaged = True
    
  def update(self):
    '''Note: animation lists are dependant on the direction, and collision'''
    
    #If the sprite is not killed#
    if not self.killed:
      self.rect.centerx -= self.speed * self.dirx
      
      #Different animation lists used. Dependant on the sprite's direction#
      if self.dirx == -1:
        self.image = self.animate.frame_images_normal[self.animate.frame]
      elif self.dirx == 1:
        self.image = self.animate.frame_images_r_normal[self.animate.frame]
    
    #If the sprite is killed#
    elif self.killed:
      self.dmg = 0
      
      if self.dirx == -1:
        self.image = self.animate.frame_images_killed[self.animate.frame_killed]
      elif self.dirx == 1:
        self.image = self.animate.frame_images_r_killed[self.animate.frame_killed]        
        
    #Updates the frames#
    self.animate.frame_update(self.killed)
         
      
class Enemy_Builder(pygame.sprite.Sprite):
  def __init__(self, counter):
    pygame.sprite.Sprite.__init__(self)
    
    '''Enemy group. Used to contain all enemy sprites'''
    self.enemies = pygame.sprite.Group()

    #Enemy attributes based on type. E.g.: enemy1, enemy2, boss#
    self.pos = [(50,-12.5), (596.5,-12.5)]
    self.damage = [1,2,10]
    
    self.counter = counter
    
  def build(self):
    
    #Calls the random method of this class#
    pos = self.random()
    
    if self.counter.enemy1_wait < 1:
      #Creates an object of the Enemy class#
      #Passes arguments: filename, frame width, frame height, damage, position, speed#
      enemy1 = Enemy("Images/Enemies/animation1.png", 27, 29, self.damage[0], pos, 5, 2, 50)
      
      #Adds enemy object to the enemy group container#
      self.enemies.add(enemy1)
      
      #Resets counter#
      self.counter.enemy1_wait += self.counter.enemy1_delay
      
    if self.counter.enemy2_wait < 1:
      enemy2 = Enemy("Images/Enemies/animation2.png", 27, 29, self.damage[1], pos, 8, 10, 100)
      self.enemies.add(enemy2)
      self.counter.enemy2_wait += self.counter.enemy2_delay
    
    if self.counter.boss_wait < 1:
      boss = Enemy("Images/Enemies/animation3.png", 27, 29, self.damage[2], pos, 2, 40, 200)
      self.enemies.add(boss)
      self.counter.boss_wait += self.counter.boss_delay
    
  def random(self):
    
    #Randomly returns a position in the list: self.pos#
    r = random.randrange(0, (len(self.pos)))
    return self.pos[r]
  
 
