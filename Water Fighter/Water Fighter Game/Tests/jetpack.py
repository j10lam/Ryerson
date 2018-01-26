import pygame, sys
from pygame.locals import *
pygame.init()

class Jetpack(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load("luma.png")
    self.image = pygame.transform.scale(self.image, (50,50))
    self.rect = self.image.get_rect()
    self.rect.center = (500,450)
    self.angle = -45            #Rotates bullet -45degrees#
    self.rotate = -45
      
    self.vel_x = 0 
    self.vel_y = 0
    self.accel = 0.125   #0.05#
    
        
  def accel_up(self):
    self.vel_y -= self.accel
    
  def accel_down(self): 
    self.vel_y += self.accel
        
  def accel_left(self):
    self.vel_x -= self.accel

  def accel_right(self):
    self.vel_x += self.accel
  
    
  def control(self, keys):
    if keys[K_a]:
      self.accel_left()
    if keys[K_d]:
      self.accel_right()
    if keys[K_SPACE] == 1:
      self.accel_up()
    if keys[K_SPACE] == 0:
      self.accel_down()
      

      
    #weapons.build(keys, self.rect.center, self.angle, timer, self.rotate)
    
  def update(self):
    self.rect.centerx += self.vel_x
    self.rect.centery += self.vel_y
    
    self.rect.top = max(self.rect.top, 0)
    self.rect.bottom = min (self.rect.bottom, 500)
    self.rect.left = max(self.rect.left, 0)
    self.rect.right = min(self.rect.right, 1000)
    
    if self.rect.bottom == 500:
      self.vel_y = 0 
  
    
  def draw(self, screen):
    screen.blit(self.image, self.rect)
    
def main():
  
  screen = pygame.display.set_mode((1000, 500))
  background = pygame.image.load("background.jpg")
  jet = Jetpack()
  
  while True:
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
                
    screen.blit(background, (0,0))
    keys = pygame.key.get_pressed()
    
    jet.control(keys)
    jet.update()
    jet.draw(screen)
    
    pygame.display.flip()
if __name__ == "__main__":
  main()
  
