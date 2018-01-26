import pygame, sys
from pygame.locals import *
from WF_weapon import *
pygame.init()

class Tank:
  def __init__(self):
    self.image = pygame.image.load("pika.png")
    self.rect = self.image.get_rect()
    self.rect.center = (500,250)
    
    self.wait = 0 
    self.delay = 20
    self.angle = -1
    self.ma, self.mi = False, True
    
    self.water = Water()
    
  def calc_ang(self):
    if self.mi:
      self.angle += 1
      if self.angle == 90:
        self.ma, self.mi = True, False
    elif self.ma:
      self.angle -= 1
      if self.angle == 0:
        self.ma, self.mi = False, True
    print "angle: %s" % (self.angle)
    
  def fire(self, tank):
    if self.wait <1:
      self.water.keys(tank)
      self.wait += self.delay
      
    for water in self.water.balloons:
      water.calcpos()

    if self.wait > 0:
      self.wait -= 1
      
  def draw(self, screen):
    for water in self.water.balloons:
      water.draw(screen)
    screen.blit(self.image, self.rect)
  
    
class Game:
  def __init__(self):
    self.screen = pygame.display.set_mode((1000, 500))
  
    self.background = pygame.image.load("background.jpg")
    self.tank = Tank()
    self.clock = pygame.time.Clock()
    
  def start(self):
  
    while True:
        self.clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
     
        self.screen.blit(self.background, (0,0))    
        self.tank.calc_ang()     
        self.tank.fire(self.tank)
        self.tank.draw(self.screen)
   
        pygame.display.flip()
        
  def control(self):
    pass
  def collision(self):
    pass
  def boundary(self):
    pass
  def sprite_handler(self):
    pass
  
  

if __name__ == "__main__":
    game = Game()
    game.start()
            