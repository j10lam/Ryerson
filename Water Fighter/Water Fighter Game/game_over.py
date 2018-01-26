import pygame, sys

class Game_Over:
  def __init__(self):
    self.bg = pygame.image.load("Images/Menu/Game_Over/game_over.jpg")
    self.button_info = [["main_menu.png", (310,220)],["try_again.png", (310,340)],["quit.png", (555,430)]]
                        
    self.buttons = []
    
  def check(self, mouse, menu):
    for button, rect_button, i in self.buttons:
      if rect_button.collidepoint(mouse.rect.topleft):
        menu.reset()
        if i == 0:
          menu.flags[0] = True
        elif i == 1:
          menu.flags[2] = True
        elif i == 2:
          sys.exit()
          
  def draw(self, screen):
    screen.blit(self.bg, (0,0))
    
    for button, rect_button, i in self.buttons:
      screen.blit(button, rect_button)
          
          