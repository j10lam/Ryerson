import pygame, sys
from pygame.locals import *

from WF_weapons import *
from WF_counter import *
from WF_monster import *
from WF_hero import *
from WF_obstacle import *
from WF_stat import *
from WF_misc import *

pygame.init()

class Game(pygame.sprite.Sprite):
  def __init__(self, menu):
    pygame.sprite.Sprite.__init__(self)
    
    ''' background '''
    self.background = pygame.image.load("Images/Backgrounds/bg02.jpg")
    self.background = pygame.transform.scale(self.background, (620, 480))
    
    ''' Objects '''
    self.counter = Counter()
    self.enemy = Enemy_Builder(self.counter)
    self.hero = Hero(self.counter)
    self.char = pygame.sprite.GroupSingle(self.hero)
    self.crate = Crate()
    self.platform = Platform()
    self.border = Border()
    self.points = Stats()
    self.menu = menu
    
    ''' Variables '''
    self.clock = pygame.time.Clock()
    self.game_running = True
        
    ''' Initial Function Calls '''
    self.border.build()

  def start(self):
    ''' Screen '''
    self.screen = pygame.display.set_mode((800, 480))
    
    while self.game_running:
      self.clock.tick(20)
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
          
      ''' Blitting background to screen '''
      self.screen.blit(self.background, (0,0))
      
      ''' Function Calls'''
      self.crate.build()
      self.enemy.build()
      self.control()
      self.boundary()
      self.gravity()     
      self.collision() 
      self.menu.sound.play()
      
      ''' Updates '''
      
      self.sprite_handler()
      self.points.draw(self.screen)
      self.counter.update()
      
      #If health runs out. go back to menu#
      if self.points.killed:
        self.menu.fix_screen = True
        #self.menu.start = True
        self.menu.sound.sound.stop()
        break
      
      ''' Display Flip '''
      pygame.display.flip()
        
  def control(self):
    self.keys = pygame.key.get_pressed()
      
  def boundary(self):
    screen_height = self.screen.get_height()
    
    for enemy in self.enemy.enemies:
      if enemy.rect.top > screen_height:
        self.enemy.enemies.remove(enemy)
        
    for crate in self.crate.crates:
      if crate.rect.top> screen_height:
        self.crate.crates.remove(crate)
        
    for hero in self.char:
      if hero.rect.top > screen_height:
        self.char.remove(hero)
        
        
  def collision(self): 
    
    '''Enemy Collisions'''
    #Weapon Collisions#
    for enemy in self.enemy.enemies:
      for weapon in self.hero.weapons.weapons:
        if pygame.sprite.spritecollide(enemy, self.hero.weapons.weapons,True):
          #Calculating damage dealt to enemy#
          enemy.hit(weapon.dmg, self.points)
 
      for weapon in self.hero.weapons.weapons2:
        if pygame.sprite.collide_rect(enemy, weapon):  
          weapon.hit = True
          enemy.hit(weapon.dmg, self.points)
          
        #Checking for finished Animation#
        if weapon.animate.done_animation:      
          self.hero.weapons.weapons2.remove(weapon)
          
        
      #Hero Collisions#                                                   
      if pygame.sprite.spritecollide(enemy, self.char, False):
        #Updating health#
        self.points.health_update(enemy.dmg)
        enemy.killed = True
        
      #Checking for finished Animation#
      if enemy.animate.done_animation:
        self.points.points_update(enemy)
        self.enemy.enemies.remove(enemy)
        
    '''Crate Collisions'''  
    if pygame.sprite.groupcollide(self.char, self.crate.crates, False, True):
      self.crate.change(self.hero.weapons)
      self.points.crates_update()

    
    ''' Platform collisions '''
    #Hero Collisions#
    for platform in self.platform.platforms:
      for hero in self.char:
        if platform.rect.collidepoint(hero.rect.midbottom):
          hero.rect.bottom = platform.rect.top
          hero.collide = True
        elif platform.rect.collidepoint(hero.rect.midtop):
          hero.rect.top = platform.rect.bottom
        elif platform.rect.collidepoint(hero.rect.midleft):
          hero.rect.left = platform.rect.right
        elif platform.rect.collidepoint(hero.rect.midright):
          hero.rect.right = platform.rect.left
          
    #Enemy Collisions#
      for enemy in self.enemy.enemies:
        if platform.rect.collidepoint(enemy.rect.midbottom):
          enemy.rect.bottom = platform.rect.top
        elif platform.rect.collidepoint(enemy.rect.midleft):
          enemy.rect.left = platform.rect.right
          enemy.dirx = -1
        elif platform.rect.collidepoint(enemy.rect.midright):
          enemy.rect.right = platform.rect.left
          enemy.dirx = 1
          
          
    #Crate Collisions#
      for crate in self.crate.crates:
        if platform.rect.collidepoint(crate.rect.midbottom):
          crate.rect.bottom = platform.rect.top     
     
    #Weapon Collision#
    pygame.sprite.groupcollide(self.hero.weapons.weapons, self.platform.platforms, True, False)  
    pygame.sprite.groupcollide(self.hero.weapons.weapons2, self.platform.platforms, True, False)
              
    ''' Border collisions '''
    for border in self.border.borders:
      for enemy in self.enemy.enemies:
        if border.rect.collidepoint(enemy.rect.midleft):
          enemy.rect.left = border.rect.right
          enemy.dirx = -1
        elif border.rect.collidepoint(enemy.rect.midright):
          enemy.rect.right = border.rect.left
          enemy.dirx = 1
          
      for hero in self.char:
        if border.rect.collidepoint(hero.rect.midleft):
          hero.rect.left = border.rect.right
        elif border.rect.collidepoint(hero.rect.midright):
          hero.rect.right = border.rect.left
      
    #Weapon Collision#
    pygame.sprite.groupcollide(self.hero.weapons.weapons, self.border.borders, True, False)
    pygame.sprite.groupcollide(self.hero.weapons.weapons2, self.border.borders, True, False)

  
  def sprite_handler(self):
    
    ''' Enemy Sprites '''
    self.enemy.enemies.update()
    self.enemy.enemies.draw(self.screen)
    
            
    ''' Weapons '''
    self.hero.weapons.weapons.update()
    self.hero.weapons.weapons.draw(self.screen)
    
    #Seperate group made for weapons that explode#
    self.hero.weapons.weapons2.update()
    self.hero.weapons.weapons2.draw(self.screen)
    
    ''' Hero Sprites '''    
    self.char.update(self.keys)
    self.char.draw(self.screen)
    
    ''' Crates '''
    self.crate.crates.draw(self.screen)
    
    ''' Platforms '''
    self.platform.platforms.draw(self.screen)
    
    ''' Borders '''
    self.border.borders.draw(self.screen)
   
  def gravity(self):
    self.hero.rect.centery += 9.8
    
    for crate in self.crate.crates:
      crate.rect.centery += 9.8
      
    for enemy in self.enemy.enemies:
      enemy.rect.centery += 9.8
      
  
