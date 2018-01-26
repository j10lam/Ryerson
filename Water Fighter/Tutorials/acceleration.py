from pygame import *

class RocketShip():
    def __init__(self, start_x, start_y):
        # position:
        self.x = start_x
        self.y = start_y
        self.ang = 0 
        # velocity: distance travelled per frame
        self.vel_x = 0
        self.vel_y = 0 
       
        # acceleration: increment that velocity is increased/decreased
        self.accel = 0.05
        
        self.img = image.load("goodship.png")
        self.img.convert()
           
    def move(self):
        self.x += self.vel_x
        self.y += self.vel_y
    def accel_right(self):
        self.vel_x += self.accel
        self.ang = 0 
    def accel_left(self):
        self.vel_x -= self.accel
        self.ang = 180
    def accel_up(self):
        self.vel_y -= self.accel
        self.ang = 90
    def accel_down(self):
        self.vel_y += self.accel
        self.ang = 270
        
    def draw(self, screen):
        image = transform.rotate(self.img, self.ang)
        screen.blit(image, (self.x, self.y))
        

init()
screen = display.set_mode((1250, 600))
clock = time.Clock()

rocket = RocketShip(10, 100)

playing = True
while playing:

    for e in event.get():
        if e.type == QUIT:
            playing = False
    
    # a list of 1's and 0's indicating which buttons are currently pressed
    list_of_keys_pressed = key.get_pressed()

    if list_of_keys_pressed[K_RIGHT] == 1:
        rocket.accel_right()
    
    if list_of_keys_pressed[K_LEFT] == 1:
        rocket.accel_left()
    if list_of_keys_pressed[K_UP] == 1:
        rocket.accel_up()
    if list_of_keys_pressed[K_DOWN] == 1:
        rocket.accel_down()
        

    rocket.move()

    screen.fill((0,0,0))
    rocket.draw(screen)
    display.flip()
    
    clock.tick(60)