import pygame, sys, pygame.mixer
from pygame.locals import*

pygame.init()

class Settings:
  def __init__(self):
    self.bg = pygame.image.load("settings.jpg")
    
    self.s = [["back.png", (500,431), 1], ["edit_keys.png", (500,275), 2], ["volume_button.png", (377,171), 3]]
    
    self.line = pygame.image.load("volume_line.png")
    self.rect_line = self.line.get_rect()
    self.rect_line.center = (505,171)
    
    self.buttons = []
    
    self.mouse = pygame.image.load("mouse.png")
    self.rect_mouse = self.mouse.get_rect()
    #self.rect_mouse.size = (1,1)
    
   
    self.sound = pygame.mixer.Sound("beast.wav")
    self.vol = 0 
    
  def build(self):
    for img, pos, i in self.s:
      button = pygame.image.load(img)
      rect_button = button.get_rect()
      rect_button.center = pos
      self.buttons.append([button, rect_button, i])
      
  def play(self):
    if self.vol != 0:
      self.sound.play()

      
  def check(self):
    self.rect_mouse.topleft = posx, posy = pygame.mouse.get_pos()
    self.mpress = pygame.mouse.get_pressed()
    
    
    for button, rect_button, i in self.buttons:
      if Rect.colliderect(self.rect_mouse, rect_button) and self.mpress == (1,0,0):

        if i == 1:
          print "back"
          
        elif i == 2:
          print "controls"
          
        elif i == 3:
          rect_button.centerx = posx
 
          rect_button.right = min(rect_button.right, self.rect_line.right)
          rect_button.left = max(rect_button.left, self.rect_line.left)
          
          self.vol = (rect_button.centerx - 377)/256.
          print "brectx: %s, vol: %s" % (rect_button.centerx, self.vol)
          self.sound.set_volume(self.vol)
      
      if Rect.colliderect(self.rect_mouse, self.rect_line) and self.mpress == (1,0,0):
        if i == 3:
          rect_button.centerx = posx
     
  
  def draw(self, screen):
    screen.blit(self.bg, (0,0))
    screen.blit(self.line, self.rect_line)
    for button, rect, i in self.buttons:
      screen.blit(button, rect)
    screen.blit(self.mouse, self.rect_mouse)
    pygame.display.flip()
      
def main():
  
  dim = width, height = 1000, 500
  screen = pygame.display.set_mode(dim)
  clock = pygame.time.Clock()
  
  settings = Settings()
  settings.build()
      

  
  while True:
    clock.tick(50)
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT: 
        sys.exit()
        
        
    settings.play()
    pygame.mixer.set_num_channels(1)
    pygame.mouse.set_visible(False)
    
    settings.check()
    settings.draw(screen)
        
if __name__ == "__main__":
  main()
  
     #if (rect_button.collidepoint(pygame.mouse.get_pos()) and self.mpress[0]):
            #print "true"