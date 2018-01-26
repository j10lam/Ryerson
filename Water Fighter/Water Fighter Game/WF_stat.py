import pygame, sys
pygame.init()

class Stats:
  def __init__(self):
    self.font = pygame.font.Font("Misc/zombie.ttf", 30)
    self.image = pygame.image.load("Images/Misc/scoreboard.png")
    self.rect = self.image.get_rect()
    self.rect.center = (710, 240)
    
    self.health = 100
    self.colour = (255, 255, 0)
    self.kills = 0 
    self.crates = 0
    self.points = 0 
    
    self.killed = False
          
  def health_update(self, dmg):
    if self.health > 0:
      self.health -= dmg
      if self.health < 51:
        self.colour = (255,0,0)
      
    elif self.health < 1:
      self.health = 0 
      self.killed = True  

  def points_update(self, enemy):
    self.points += enemy.points
    
  def kills_update(self):
    self.kills += 1
    
  def crates_update(self):
    self.crates += 1
    
  def update(self):
    if not self.killed:
      self.health_label = self.font.render(str(self.health), 50, self.colour)
      self.kills_label = self.font.render(str(self.kills), 50, (255, 255, 0))
      self.crates_label = self.font.render(str(self.crates), 50, (255, 255, 0))
      self.points_label = self.font.render(str(self.points), 50, (255, 255, 0))

  def draw(self, screen):     
    self.update()
    
    screen.blit(self.image, self.rect)
    screen.blit(self.health_label, (710, 54))
    screen.blit(self.crates_label, (710, 95))
    screen.blit(self.kills_label, (710, 130))
    screen.blit(self.points_label, (710, 165))

