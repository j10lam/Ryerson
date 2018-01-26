import pygame, sys
from pygame.locals import * 
pygame.init()

class Background(pygame.sprite.Sprite):
  def __init__(self):
    self.moving = True
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load("bg2.jpg").convert()
    self.rect = self.image.get_rect()
    self.dx = 5
  
    
      
  def update(self):
    key = pygame.key.get_pressed()
    
    if self.moving:
      if key[K_RIGHT]:
        self.rect.left -= self.dx
      
    if self.rect.right <= 1000:
      self.moving = False 
      
  def reset(self):
    self.rect.left = 0

  def draw(self, screen):
    screen.blit(self.image, self.rect)
  
def main():
  
  dim = width, height = 1000, 500
  screen = pygame.display.set_mode(dim)
  pygame.display.set_caption("Water Fighter")
  clock = pygame.time.Clock()
  
  background = Background()
  while True:
    clock.tick(50)
    for event in pygame.event.get():
      if event.type == pygame.QUIT :
        sys.exit()
        
    background.draw(screen)
   
    background.update()
    
    pygame.display.flip()
if __name__ == "__main__":
  main()