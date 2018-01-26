import pygame, sys

class Button_Builder:
  def __init__(self):    
    self.identifier = 0
    
  def build(self, images, path, buttons):
    self.identifier = 0
    for image, pos in images:
      button = pygame.image.load(path + image)
      rect_button = button.get_rect()
      rect_button.center = pos
      
      buttons.append([button, rect_button, self.identifier])
    
      self.identifier += 1        