import pygame, sys

class Main_Menu:
  def __init__(self):
    self.bg = pygame.image.load("Images/Menu/Main_Menu/main_menu.jpg")
    
    
    self.button_info = [["start.png",(235,225)],["setting.png",(385,225)],["instructions.png", (235, 345)],["quit.png", (385,345)]]
    
    self.buttons = []
  
  def check(self, mouse, menu):
    for button, rect_button, i in self.buttons:
      if rect_button.collidepoint(mouse.rect.topleft):
        menu.reset()
        if i == 0:
          menu.flags[2] = True
        elif i == 1: 
          menu.flags[1] = True
        elif i == 2:
          menu.flags[3] = True
        elif i == 3:
          sys.exit()
    
  def draw(self, screen):
    screen.blit(self.bg, (0,0))
    
    for button, rect_button, i in self.buttons:
      screen.blit(button, rect_button)
    