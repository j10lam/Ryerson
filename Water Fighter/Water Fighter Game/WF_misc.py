import pygame, math, random
from pygame.locals import *

class Crate(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load("Images/Misc/crate.png")
    self.image = pygame.transform.scale(self.image, (20, 20))
    self.rect = self.image.get_rect()
    self.rect.center = (random.randint(20,600),random.randint(30, 410))
    self.crates = pygame.sprite.Group()
    
  def build(self):
    #Builds a crate if no crates in group#
    if not bool(self.crates):
      crate = Crate()
      self.crates.add(crate)
    
  def update(self):
    self.rect.centery += 9.8
    
    
  def change(self, weapons):
    #Resets the weapons, making all weapons False#
    weapons.reset()
    
    random_numb = random.randrange(0, (len(weapons.weapons_list))) 
    weapons.weapons_list[random_numb] = True 
    #A random item in the list: weapoans_list, will become true#
    
class Sound:
  def __init__(self):
    self.sound = pygame.mixer.Sound("Misc/ace.wav")
    self.vol = 0 
    
  def play(self):
    if self.vol != 0:
      self.sound.play(-1)
    #Refrains number of songs played#
    pygame.mixer.set_num_channels(1)
  
  def change_vol(self, vb):
    #Calculate and sets volume#
    self.vol = (vb.centerx - 267)/256.
    self.sound.set_volume(self.vol)
    
class Mouse:
  def __init__(self):
    self.mouse = pygame.image.load("Images/Misc/mouse.png")
    self.rect = self.mouse.get_rect()
    
  def update(self):
    self.rect.topleft = pygame.mouse.get_pos()
    self.mpress = pygame.mouse.get_pressed()
  
  def draw(self, screen):
    screen.blit(self.mouse, self.rect) 