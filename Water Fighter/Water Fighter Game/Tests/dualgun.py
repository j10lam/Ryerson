import pygame, sys
from pygame.locals import *
pygame.init()

class Dual(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load("bb.png")
    self.image = pygame.transform.scale(self.image, (25,25))
    self.rect = self.image.get_rect()
    self.b_left = pygame.sprite.Group()
    self.b_right = pygame.sprite.Group()
    
    
  def build(self, pos):
    bullet_left = Dual()
    bullet_left.image = pygame.transform.flip(bullet_left.image, 90, 0)

    bullet_right = Dual()
    bullet_left.rect.center = pos
    bullet_right.rect.center = pos

    self.b_left.add(bullet_left)
    self.b_right.add(bullet_right)
    
  def update_left(self):
    self.rect.centerx -= 5
  
  def update_right(self):
    self.rect.centerx += 5
    

    
def main():
  screen = pygame.display.set_mode((1000, 500))
  background = pygame.image.load("bg02.jpg")
  background = pygame.transform.scale(background, (1000,500))
  
  dual = Dual()
  
  while True:
     
    screen.blit(background, (0,0))

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
    
    keys = pygame.key.get_pressed()
    if keys[K_q]:
      dual.build((500,250))
      
      
    dual.b_left.clear(screen, background)
    for bullet in dual.b_left.sprites():
      bullet.update_left()
    dual.b_left.draw(screen)
    
    dual.b_right.clear(screen, background)
    for bullet in dual.b_right.sprites():
      bullet.update_right()
    dual.b_right.draw(screen)
    
    pygame.display.flip()
    
    
if __name__ == "__main__":
  main()
  
  