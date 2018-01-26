import pygame, sys
from pygame.locals import *
pygame.init()

class Rocket:
  def __init__(self):
    self.rocket = pygame.image.load("megaman.png")
    self.rect = self.rocket.get_rect()
    
    self.screen = pygame.image.load("bg.jpg")
    
    self.gravity = 5
  
  def update(self, keys):
    if keys[K_a]:
      self.rect.centerx -= 15
    if keys[K_d]:
      self.rect.centerx += 15

    if keys[K_w]:
      self.rect.centery -= 15
    if keys[K_s]:
      self.rect.centery += 15
      
    #self.rect.centery += self.gravity 
    
  def draw(self, screen):
    screen.blit(self.screen, (0,0))
    screen.blit(self.rocket, self.rect) 
    pygame.display.flip()
    
    
def main():
  
  dim = width, height = 1000, 500
  screen = pygame.display.set_mode(dim)
  clock = pygame.time.Clock()
  
  rocket = Rocket()
  
  while True:
    clock.tick(50)
    
    keys = pygame.key.get_pressed()
    rocket.update(keys)
    rocket.draw(screen)

    for event in pygame.event.get():
      if event.type == pygame.QUIT: 
        sys.exit()
        
   
if __name__ == "__main__":
  main()

