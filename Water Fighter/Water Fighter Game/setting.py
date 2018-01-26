import pygame

class Settings:
  def __init__(self):
    self.bg = pygame.image.load("Images/Menu/Setting/setting.jpg")
    
    self.button_info = [["back.png", (320,322)], ["volume_button.png", (267,207)]]
    
    self.line = pygame.image.load("Images/Menu/Setting/volume_line.png")
    self.rect_line = self.line.get_rect()
    self.rect_line.midleft = (255,207)
    
    self.buttons = []
    
      
  def check(self, mouse, menu):   
    for button, rect_button, i in self.buttons:
      
      if rect_button.collidepoint(mouse.rect.topleft):
        if i == 0: 
          menu.reset()
          menu.flags[0] = True  
          
        elif i == 1:
          #Moves and restricts volume button's location#
          rect_button.centerx = mouse.rect.topleft[0]
          self.calculate(rect_button, menu)
          
  def check2(self, mouse, menu): 
    for button, rect_button, i in self.buttons:
      
      if self.rect_line.collidepoint(mouse.rect.topleft) and mouse.mpress[0]:
        if i == 1:
          rect_button.centerx = mouse.rect.topleft[0]
          self.calculate(rect_button, menu)

  def calculate(self, rect_button, menu):
    #Allows for either clicking volume line, or volume button to change volume#
  
    rect_button.right = min(rect_button.right, self.rect_line.right)
    rect_button.left = max(rect_button.left, self.rect_line.left)
      
    #Changes the volume#
    menu.sound.change_vol(rect_button)

  def draw(self, screen):
    screen.blit(self.bg, (0,0))
    screen.blit(self.line, self.rect_line)
    for button, rect, i in self.buttons:
      screen.blit(button, rect)
