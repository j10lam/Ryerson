import pygame, sys, pygame.mixer
from pygame.locals import*
from menu_build import *
from setting import *
from instruction import *
from main_menu import *
from level_selection import *
from game_over import *

from WF_misc import *
pygame.init()

class Menu:
  def __init__(self):
    #Contains a list of flags for different menues#
    self.flags = [True, False, False, False, False]
    
    self.main_menu = Main_Menu()
    self.setting = Settings()
    self.level_selection = Level_Selection()
    self.instruction = Instructions()
    self.game_over = Game_Over()
   
    self.mouse = Mouse()
    self.sound = Sound()
    
    #Creates the buttons for each menu#
    self.button_builder = Button_Builder()
    
    self.start = True
    self.fix_screen = True

  def build(self):
    self.button_builder.build(self.setting.button_info, "Images/Menu/Setting/", self.setting.buttons)
    self.button_builder.build(self.main_menu.button_info, "Images/Menu/Main_Menu/", self.main_menu.buttons)
    self.button_builder.build(self.level_selection.button_info, "Images/Menu/Level_Selection/", self.level_selection.buttons)
    self.button_builder.build(self.game_over.button_info, "Images/Menu/Game_Over/", self.game_over.buttons)
  
  '''Checks Flags. If True, checks and draws menue corresponding to that bool''' 
  def update(self, menu):
    if self.flags[0]:
      self.main_menu.check(self.mouse, menu)
    elif self.flags[1]:
      self.setting.check(self.mouse, menu)
    elif self.flags[2]:
      self.level_selection.check(self.mouse, menu)
    elif self.flags[3]:
      self.instruction.check(self.mouse, menu)
    elif self.flags[4]:
      self.game_over.check(self.mouse, menu)
  
  def update2(self, menu):
    if self.flags[1]:
      self.setting.check2(self.mouse, menu)
    
  def draw(self, screen):
    if self.flags[0]:
      self.main_menu.draw(screen)
    elif self.flags[1]:
      self.setting.draw(screen)
    elif self.flags[2]:
      self.level_selection.draw(screen)
    elif self.flags[3]:
      self.instruction.draw(screen)
    elif self.flags[4]:
      self.game_over.draw(screen)

    self.mouse.draw(screen)
    pygame.display.flip()
    
  def reset(self):
    #Sets all Flags in the list of flags to False#
    for menu in range(len(self.flags)):
      self.flags[menu] = False
      
  def begin(self):    
    dim = width, height = 620, 480
    self.screen = pygame.display.set_mode(dim)
    self.clock = pygame.time.Clock()
    
    self.menu = Menu()
    self.menu.build()
    

    pygame.display.set_caption("Water Fighter")
    
    while self.menu.start:
      if self.menu.fix_screen:
        self.screen = pygame.display.set_mode(dim)
        self.menu.fix_screen = False
  
      self.clock.tick(20)
      
      pygame.mouse.set_visible(False)
      
      for event in pygame.event.get():
        if event.type == pygame.QUIT: 
          sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
          self.menu.update(self.menu)
          
      self.menu.mouse.update()
      self.menu.update2(self.menu)
      self.menu.draw(self.screen)
    
