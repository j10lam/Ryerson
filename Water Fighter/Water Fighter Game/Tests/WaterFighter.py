import pygame, sys
from pygame.locals import *
from WF_weapons import *
from timer import *
from WF_monster import *
from WF_Hero import *
from platform import *
pygame.init()


class Game(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    
    ''' screen, background '''
    self.screen = pygame.display.set_mode((1000, 500))
    self.background = pygame.image.load("bg02.jpg")
    
    ''' Objects '''
    self.enemy = Enemy()
    self.timer = Timer()
    self.hero = Hero_control()
    self.crate = Crate()
    self.ground = Ground()
    self.platform = Platform()
    self.border = Border()
    
    ''' Variables '''
    self.clock = pygame.time.Clock()
        
    ''' Initial Function Calls '''
    self.enemy.build(5)
    self.crate.build(1)
    self.platform.build()
    self.border.build()
    
  def start(self):
    
    while True:
      self.clock.tick(20)
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
 
      ''' Blitting background to screen '''
      self.screen.blit(self.background, (0,0))
      
      ''' Function Calls'''
      self.ground.draw(self.screen)
      self.control()
      self.collision()   # Fix Collision Glitch #
      
      ''' Updates '''
      self.sprite_handler()
      self.hero.update(self.keys, self.timer)
      self.gravity()
      self.timer.update()
        
      
      ''' Display Flip '''
      pygame.display.flip()
        
  def control(self):
    self.keys = pygame.key.get_pressed()
         
  def collision(self): 
    
    ''' Weapon collisions '''
    pygame.sprite.groupcollide(self.hero.weapons.balloons, self.enemy.enemies, False, True)
    pygame.sprite.groupcollide(self.hero.weapons.bullets, self.enemy.enemies, True, True)
    pygame.sprite.groupcollide(self.hero.weapons.dual_right, self.enemy.enemies, True, True)
    pygame.sprite.groupcollide(self.hero.weapons.dual_left, self.enemy.enemies, True, True)
    
    ''' Hero collisions '''
    pygame.sprite.groupcollide(self.hero.char, self.enemy.enemies, False, True)
    if pygame.sprite.groupcollide(self.hero.char, self.crate.crates, False, True):
      self.hero.weapons.reset()
      self.crate.random(self.hero.weapons.weapons)
    
    ''' Platform collisions '''
    
    ''' With Hero '''
    for platform in self.platform.platforms.sprites():
      for hero in self.hero.char.sprites():
        if platform.rect.collidepoint(hero.rect.midbottom):
          hero.rect.bottom = platform.rect.top
          hero.collide = True
        elif platform.rect.collidepoint(hero.rect.midtop):
          hero.rect.top = platform.rect.bottom
        elif platform.rect.collidepoint(hero.rect.midleft):
          hero.rect.left = platform.rect.right
        elif platform.rect.collidepoint(hero.rect.midright):
          hero.rect.right = platform.rect.left
          
    ''' With Enemies '''
    for platform in self.platform.platforms.sprites():
      for enemy in self.enemy.enemies.sprites():
        if platform.rect.collidepoint(enemy.rect.midbottom):
          enemy.rect.bottom = platform.rect.top
        elif platform.rect.collidepoint(enemy.rect.midleft):
          enemy.rect.left = platform.rect.right
        elif platform.rect.collidepoint(enemy.rect.midright):
          enemy.rect.right = platform.rect.left
          
    ''' Crate collisions '''
    for platform in self.platform.platforms.sprites():
      for crate in self.crate.crates.sprites():
        if platform.rect.collidepoint(crate.rect.midbottom):
          crate.rect.bottom = platform.rect.top     
    
    ''' Ground collisions '''
    for hero in self.hero.char.sprites():
      if Rect.colliderect(self.ground.rect, hero.rect):
        hero.rect.bottom = self.ground.rect.top
        hero.collide = True
    for crate in self.crate.crates.sprites():
      if Rect.colliderect(self.ground.rect, crate.rect):
        crate.rect.bottom = self.ground.rect.top
    for enemy in self.enemy.enemies.sprites():
      if Rect.colliderect(self.ground.rect, enemy.rect):
        enemy.rect.bottom = self.ground.rect.top

        
    ''' Border collisions '''
    for border in self.border.borders.sprites():
      for enemy in self.enemy.enemies.sprites():
        if border.rect.collidepoint(enemy.rect.midleft):
          enemy.rect.left = border.rect.right
          enemy.dirx = -1
          enemy.flip = True
        elif border.rect.collidepoint(enemy.rect.midright):
          enemy.rect.right = border.rect.left
          enemy.dirx = 1
          enemy.flip = True
          
    for border in self.border.borders.sprites():
      for hero in self.hero.char.sprites():
        if border.rect.collidepoint(hero.rect.midleft):
          hero.rect.left = border.rect.right
        elif border.rect.collidepoint(hero.rect.midright):
          hero.rect.right = border.rect.left
          
   
  def boundary(self):
    pass
  
  def sprite_handler(self):
    
    ''' Enemy Sprites '''
    #self.enemy.enemies.clear(self.screen, self.background)
    self.enemy.enemies.update()
    self.enemy.enemies.draw(self.screen)
            
    ''' Weapons '''
    #self.hero.weapons.balloons.clear(self.screen, self.background)
    self.hero.weapons.balloons.update()
    self.hero.weapons.balloons.draw(self.screen)
    
    #self.hero.weapons.bullets.clear(self.screen, self.background)
    self.hero.weapons.bullets.update(self.hero.checks[2])
    self.hero.weapons.bullets.draw(self.screen)
    
    #self.hero.weapons.dual_left.clear(self.screen, self.background)
    for bullet in self.hero.weapons.dual_left.sprites():
      bullet.update_left()
    self.hero.weapons.dual_left.draw(self.screen)
    
    #self.hero.weapons.dual_right.clear(self.screen, self.background)
    for bullet in self.hero.weapons.dual_right.sprites():
      bullet.update_right()
    self.hero.weapons.dual_right.draw(self.screen)
      
    
    ''' Hero Sprites '''    
    #self.hero.char.clear(self.screen, self.background)
    self.hero.char.update()
    self.hero.char.draw(self.screen)
    
    ''' Crates '''
    #self.crate.crates.clear(self.screen, self.background)
    self.crate.crates.draw(self.screen)
    
    ''' Platforms '''
    #self.platform.platforms.clear(self.screen, self.background)
    self.platform.platforms.draw(self.screen)
    
    ''' Borders '''
    #self.border.borders.clear(self.screen, self.background)
    self.border.borders.draw(self.screen)
   
  def gravity(self):
    if self.hero.checks[0]:
      self.hero.hero.rect.centery += 9.8
    
    for crate in self.crate.crates.sprites():
      crate.rect.centery += 9.8
      
    for enemy in self.enemy.enemies.sprites():
      enemy.rect.centery += 9.8
  
if __name__ == "__main__":
    game = Game()
    game.start()