import pygame, sys
from WF_game import *

class Level_Selection:
  def __init__(self):
    self.bg = pygame.image.load("Images/Menu/Level_Selection/level_selection.jpg")
    self.button_info = [["back.png", (555,430)],["level_box1.png", (235,220)],["level_box2.png", (385,220)],\
                        ["level_box3.png", (235,346)],["level_box4.png", (385,346)]]
    self.buttons = []
    
  def check(self, mouse, menu):
    for button, rect_button, i in self.buttons:
      if rect_button.collidepoint(mouse.rect.topleft):
        menu.reset()
        #Creates the Game object#
        menu.game = Game(menu)
        if i == 0:
          menu.reset()
          menu.flags[0] = True
        elif i == 1: 
          menu.game.platform.build(0)
        elif i == 2:
          menu.game.platform.build(1)
        elif i == 3:
          menu.game.platform.build(2)
        elif i == 4:
          menu.game.platform.build(3)
          
        #Resets menu, sets True flag for level selection, etc#
        if (i == 1) or (i == 2) or (i == 3) or (i == 4):
          menu.reset()
          menu.flags[4] = True
          #menu.start = False
        
          #Starts the game object#
          menu.game.start()
        
  def draw(self, screen):
    screen.blit(self.bg, (0,0))
    
    for button, rect_button, i in self.buttons:
      screen.blit(button, rect_button)