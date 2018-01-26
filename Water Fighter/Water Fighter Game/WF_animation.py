import pygame, sys
from pygame.locals import *
pygame.init()

class Animation:
  def __init__(self, frame_width, frame_height, filename):
    self.master_image = pygame.image.load(filename)  #.convert_alpha()#
    self.master_width, self.master_height = self.master_image.get_size()
    self.frame_width, self.frame_height = frame_width, frame_height
    
    self.frame = 0 
    self.frame_killed = 0 
    self.frame_images = []
    self.frame_images_r = []
    self.counter = 0 
    self.create_image_list()
    self.done_animation = False
    
  def create_image_list(self):
    for frame_number in range(self.master_width/self.frame_width):
      posx = frame_number * self.frame_width
      posy = 0 
      frame_image = self.master_image.subsurface(posx, posy, self.frame_width, self.frame_height)
      
      #Flips the frame_image#
      frame_image_r = pygame.transform.flip(frame_image, 90, 0)
      
      #Appending to lists of animations#      
      self.frame_images.append(frame_image)
      self.frame_images_r.append(frame_image_r)

    #Splitting a whole list into two. One for normal, one for hit/killed#
    self.frame_images_normal = self.frame_images[:4]
    self.frame_images_killed = self.frame_images[4:]
         
    #The same above, exept fliped items#
    self.frame_images_r_normal = self.frame_images_r[:4]
    self.frame_images_r_killed = self.frame_images_r[4:]
    
      
  def frame_update(self, killed):
    #Limits the number of frames per frame#
    if self.counter == 2:
      
      #If sprite is not killed#
      if not killed:
	self.frame += 1
	#Constant animation loop#
	if self.frame >= len(self.frame_images_normal):
	  self.frame = 0
	  
      #If the sprite is killed#
      elif killed:
	if not self.done_animation:
	  self.frame_killed += 1
	  if self.frame_killed >= len(self.frame_images_killed):
	    self.done_animation = True
	    #Once killed animations finish, a bool becomes True#
	    #Bool used to remove finished sprites from group#
	    
      self.counter = 0 
      
    self.counter += 1
