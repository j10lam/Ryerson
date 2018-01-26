import pygame, sys
from pygame.locals import *
pygame.init()

class Jetpack(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load("luma.png")
    self.image = pygame.transform.scale(self.image, (50,50))
    self.rect = self.image.get_rect()
    self.rect.center = (100, 300)
      
    self.vel_x = 0 
    self.vel_y = 0
    self.accel = 0.5
    self.jump = False
            
  def accel_left(self):
    self.vel_x = -5

  def accel_right(self):
    self.vel_x = 5
  
  def accel_up(self):
    if not self.jump:
      self.vel_y = -10
    
  def control(self, keys):
    
    if keys[K_a] and keys[K_d]:
      self.vel_x = 0 
      
    elif keys[K_a]:
      self.accel_left()
     
    elif keys[K_d]:
      self.accel_right()

    if keys[K_SPACE]:
      self.accel_up()
      self.jump = True         
    
  def update(self):
    
    self.rect.centerx += self.vel_x
    self.rect.centery += self.vel_y
    
     # in mid air #
    if self.rect.bottom < 500:
      self.vel_y += self.accel
      
    # Landing #
    elif self.rect.bottom > 500:
      self.jump = False
      self.rect.bottom = 500
      self.vel_y = 0 
      
    # Stop moving automatically #            
    if not self.jump:
      self.vel_x = 0 
    
  def draw(self, screen):
    screen.blit(self.image, self.rect)
    
def main():
  
  screen = pygame.display.set_mode((1000, 500))
  background = pygame.image.load("bg01.jpg")
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
  
