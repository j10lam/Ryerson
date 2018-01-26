import pygame, sys, random
from pygame.locals import *
pygame.init()

class Enemy(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load("enemy.png")
    self.image = pygame.transform.scale(self.image, (25,25))
    self.rect = self.image.get_rect()
    self.enemies = pygame.sprite.Group()
    self.dirx = 1
    self.flipx = 90
    self.flip = False
    
    self.counter = 0 
    
  def build(self, qty):
    for n in range(qty):
      self.enemy = Enemy()
      self.enemy.rect.center = (random.randint(700,800), 0)
      self.enemies.add(self.enemy)
      
  def move(self):
    self.rect.centerx -= 5 * self.dirx
    
    
  def update(self):
    self.move()
    if self.flip:
      self.image = pygame.transform.flip(self.image, self.flipx, 0)
      self.flip = False
    
def main():
  
  screen = pygame.display.set_mode((1000, 500))
  
  background = pygame.image.load("background.jpg")
  enemy = Enemy()
  enemy.build(4)
  clock = pygame.time.Clock()
  while True:
      clock.tick(30)
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              sys.exit()
              
      screen.blit(background, (0, 0))
      enemy.enemies.clear(screen, background)
      enemy.enemies.update()
      enemy.enemies.draw(screen)

      pygame.display.flip()
  

if __name__ == "__main__":
    main()
            