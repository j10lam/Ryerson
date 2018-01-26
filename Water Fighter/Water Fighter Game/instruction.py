import pygame

class Instructions:
  def __init__(self):
    self.image = pygame.image.load("Images/Menu/Instructions/instruction.jpg")
    
    self.button = pygame.image.load("Images/Menu/Instructions/back.png")
    self.rect = self.button.get_rect()
    self.rect.center = (555, 430)
    
  def check(self, mouse, menu):
    if self.rect.collidepoint(mouse.rect.topleft):
      menu.reset()
      menu.flags[0] = True #flags[0] = main menu#
      
  def draw(self, screen):
    screen.blit(self.image, (0,0))
    screen.blit(self.button, self.rect)
    
    