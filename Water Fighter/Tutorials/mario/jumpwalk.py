from pygame import *

class Player:
    def __init__(self, bottomleft):
        self.img = image.load("mario.png")        
        self.box = Rect(0, 0, 0, 0,)
        self.box.bottomleft = bottomleft
        r = self.img.get_rect()
        self.box.size = r.size
        
        self.jumping = False
        self.vx, self.vy = 0, 0
        self.accel = 0.5

    
    def update(self): 
        print ("y: %s, vely: %s, total: %s")% (self.box.y, self.vy, self.box.y + self.vy)
        
        
        self.box.x += self.vx
        self.box.y += self.vy 
        
        #in mid-air
        if self.box.bottom < 800:
            self.vy += self.accel
        #landing back on ground
        elif self.box.bottom > 800:
            self.jumping = False
            self.box.bottom = 800
            self.vy = 0
        
        #momentum carries Mario when he is in mid-air
        if not self.jumping:
            self.vx = 0

    def draw(self, screen):
        screen.blit(self.img, (self.box.x, self.box.y))

    def left(self):
        self.vx = -5
    
    def right(self):
        self.vx = 5

    def jump(self):
        if not self.jumping:
            self.jumping = True
            self.vy = -18

#class Block:
    #def __init__(self, bottomleft):
        #self.box = Rect(0, 0, 0, 0)
        #self.box.bottomleft = bottomleft
        #self.img = image.load("texture.png")
        #r = self.img.get_rect()
        #self.box.size = r.size
    
    #def draw(self, screen):
        #screen.blit(self.img, self.box.topleft)
    
init()
screen = display.set_mode((1000, 800))
my_clock = time.Clock()

mario = Player((500, 800))
#platform = Block((600, 700))

playing = True
while playing:
    
    for e in event.get():
        if e.type == QUIT:
            playing = False
    
    keys_pressed = key.get_pressed()
    
    if (keys_pressed[K_LEFT] == 1) and (keys_pressed[K_RIGHT] == 0):
        mario.left()
    if (keys_pressed[K_RIGHT] == 1) and (keys_pressed[K_LEFT] == 0):
        mario.right()
    if keys_pressed[K_UP] == 1:
        mario.jump()

    #platform.draw(screen)

    mario.update()
    mario.draw(screen)
    
    display.flip()

    my_clock.tick(30)