import pygame, sys
from pygame.locals import *
pygame.init()

class Rocket(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)

    self.image = pygame.image.load("rocket.png")
    self.image = pygame.transform.scale(self.image, (25,25))
    self.image = pygame.transform.rotate(self.image, -90)
    self.rect = self.image.get_rect()
    self.pos = []
    self.frame = 0 
    
    self.smoke = Smoke()
    
  def build(self, pos, rockets):
    rocket = Rocket()
    rocket.rect.center = pos
    rockets.add(rocket)
    
  def update(self):
    self.pos.append(self.rect.midleft)
    self.rect.centerx += 5
    self.smoke.build(self.pos, self.frame)
    self.frame += 1
    
class Smoke(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load("smoke.png")
    self.image = pygame.transform.scale(self.image, (20,20))
    self.rect = self.image.get_rect()
    self.smokes = pygame.sprite.Group()
    self.counter = 0
    
  def build(self, pos, frame):
    smoke = Smoke()
    smoke.rect.center = pos[frame]
    self.smokes.add(smoke)
    self.counter += 1
    

  def update(self):
    if self.counter == 4:
      for smokes in self.smokes.sprites():
        self.smokes.remove(smokes) 
        self.counter = 0 
    
  
def main():
  screen = pygame.display.set_mode((1000, 500))
  background = pygame.image.load("bg01.jpg")
  background = pygame.transform.scale(background, (1000,500))
  
  rocket = Rocket()
  rockets = pygame.sprite.GroupSingle()
  
  while True:
     
    screen.blit(background, (0,0))

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
    
    keys = pygame.key.get_pressed()
    if keys[K_q]:
      rocket.build((300,200), rockets)
    
    rockets.clear(screen, background)
    rockets.update()
    rockets.draw(screen)
    
    for rocket in rockets.sprites():
      #smoke.build(rocket)
      
      if rocket.rect.right > 900:
        rockets.empty()
        rocket.smoke.smokes.empty()
        
    rocket.smoke.smokes.clear(screen, background)
    rocket.smoke.update()
    rocket.smoke.smokes.draw(screen)

    
    
    
    
    pygame.display.flip()
    
    
if __name__ == "__main__":
  main()
  
  