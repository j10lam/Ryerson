import pygame, sys
from pygame.locals import *
pygame.init()
class Animation:
  def __init__(self, frame_width, frame_height, filename):
    self.master_image = pygame.image.load(filename)  #.convert_alpha()#
    self.master_width, self.master_height = self.master_image.get_size()
    self.frame_width, self.frame_height = frame_width, frame_height
    
    self.frame = 0 
    self.frame_images = []
    
  def create_image_list(self):
    for frame_number in range(self.master_width/self.frame_width):
      posx = frame_number * self.frame_width
      posy = 0 
      frame_image = self.master_image.subsurface(posx, posy, self.frame_width, self.frame_height)
      self.frame_images.append(frame_image)
      
  def frame_update(self):
    self.frame += 1
    if self.frame >= len(self.frame_images):
      self.frame = 0
    
    
def main():
  #initialization
  pygame.init()
  screen = pygame.display.set_mode((640, 480))    
  background = pygame.Surface(screen.get_size())
  background = background.convert()
  screen.blit(background, (0,0))
  fps = 5
  
  #setup explosion animation
  #explosion_images = load_animation_images(46, 44, 'enemy1.png')
  #explosion_images = load_animation_images(60, 62, 'enemy2.png')
  #explosion_images = load_animation_images(66, 65, 'smoke.png')
  
  animation = Animation(60, 62, 'enemy2.png')
  animation.create_image_list()
  
  
  clock = pygame.time.Clock()
  keepGoing = True
  frame = 0
  while keepGoing:
    #restrict frame rate
    clock.tick(fps)
    screen.blit(background, (0,0))

    #listen for quit events
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
	keepGoing = False

   
    screen.blit(animation.frame_images[animation.frame], (300,300))
    
    #cycle through all the frames in the animation over and over
    
    animation.frame_update()
	
    pygame.display.flip()
      
if __name__ == "__main__":
  main()
