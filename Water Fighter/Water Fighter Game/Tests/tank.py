import pygame

class Tank(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load("pika.png")
    self.rect = self.image.get_rect()
    self.rect.center = (500,400)
   
    self.angle = -1
    self.ma, self.mi = False, True
        
  def calc_ang(self):
    if self.mi:
      self.angle += 1
      if self.angle == 90:
        self.ma, self.mi = True, False
        
    elif self.ma:
      self.angle -= 1
      if self.angle == 0:
        self.ma, self.mi = False, True
    
  def fire(self, key, weapons, timer):
    weapons.control(key, self.rect.center, self.angle, timer)
      
        
  def update(self, key, weapons, timer):
    self.calc_ang()
    self.fire(key, weapons, timer)
    
    

            