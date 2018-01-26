import pygame

def load_animation_images(frame_width, frame_height, filename):
    """returns a list of images from a graphics file"""
    frame_images = []
    master_image = pygame.image.load(filename)
    master_image.convert_alpha()
    (master_width, master_height) = master_image.get_size()
    
    #put separate frames from the graphics file into a list of images
    for frame_number in range( master_width / frame_width ):
	x = frame_number * frame_width
	y = 0
	frame_image = master_image.subsurface(x, y, frame_width, frame_height)
	frame_images.append(frame_image)

    return frame_images

#initialization
pygame.init()
screen = pygame.display.set_mode((640, 480))    
background = pygame.Surface(screen.get_size())
background = background.convert()
screen.blit(background, (0,0))
fps = 10

#setup explosion animation
explosion_images = load_animation_images(20, 20, 'explosion-sprites.png')
explosion_sprite = pygame.sprite.Sprite()
explosion_sprite.rect = (50, 50)
explosion_group = pygame.sprite.Group(explosion_sprite)

clock = pygame.time.Clock()
keepGoing = True
frame = 0
while keepGoing:
    #restrict frame rate
    clock.tick(fps)
    
    #listen for quit events
    for event in pygame.event.get():
	if event.type == pygame.QUIT:
	    keepGoing = False

    #get the next frame of the animation ready
    explosion_sprite.image = explosion_images[frame]
    explosion_group.clear(screen, background)
    explosion_group.draw(screen)
    
    pygame.display.flip()
    
    #cycle through all the frames in the animation over and over
    frame += 1
    if frame >= len(explosion_images):
	frame = 0
