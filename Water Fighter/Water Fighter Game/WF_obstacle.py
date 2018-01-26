import pygame, sys
pygame.init()

class Platform(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load("Images/Platforms/platform1.png")
    self.rect = self.image.get_rect()
    self.platforms = pygame.sprite.Group()

    self.pos1 = [(70,10), (190,10), (430,10), (550, 10),\
                (180,150), (300,150), (420,150),\
                (70,250), (550,250),\
                (180,350), (300,350), (420,350),\
                (70,450), (550,450),\
                (70,470), (190,470), (430,470), (550,470)]
    
    self.pos2 = [(70,10), (190,10), (430,10), (550, 10),\
                (300,80),\
                (180,150), (420,150),\
                (70,250), (300,250), (550,250),\
                (180,350), (300,350), (420,350),\
                (70,450), (550,450),\
                (70,470), (190,470), (430,470), (550,470)]
    
    self.pos3 = [(70,10), (190,10), (430,10), (550,10),\
                 (190,150), (310,150), (430,150),\
                 (70,250), (550,250),\
                 (190,350), (430,350),\
                 (70,430), (310,430), (550, 430),\
                 (70,450), (550,450),\
                 (250,450), (370,450),\
                (70,470), (550,470),\
                (250,470), (370,470)]
          
    self.pos4 = [(70,10), (190,10), (430,10), (550,10),\
                 (70,90), (190,110), (310,130), (430,150),\
                 (550,220),\
                 (190,280), (310,260), (430,240),\
                 (70,350),\
                 (190,370), (310,390), (430,410),\
                 (70,470), (190,470), (310,470), (430,470), (550,470)]


    self.pos = [self.pos1, self.pos2, self.pos3, self.pos4]
    
  def build(self,n):
    for pos in self.pos[n]:
      platform = Platform()
      platform.rect.center = pos
      self.platforms.add(platform)
      
class Border(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load("Images/Borders/border1.png")
    self.rect = self.image.get_rect()
    self.borders = pygame.sprite.Group() 
    
    self.border = [(5,480), (615, 480)]
    
    self.counter = 0 
    
  def build(self):
    for x,y in self.border:
      border = Border()
      border.rect.centerx = x
      border.rect.bottom = y
      if self.counter == 1:
        border.image = pygame.transform.flip(border.image, 90, 0)
        
      self.borders.add(border)
      self.counter += 1
    