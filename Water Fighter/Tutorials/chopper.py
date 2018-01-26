""" chopper.py 
    illustrates chopping several images
    from a master image to make an animation.
    Uses heli.bmp from SpriteLib
"""

import pygame
pygame.init()

class Chopper(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.loadImages()
        
        self.frame = 0
        self.delay = 3
        self.pause = 0

        self.image = self.imgList[0]
        self.rect = self.image.get_rect()
        self.rect.size = (100,50)
        
    def loadImages(self):
        imgMaster = pygame.image.load("heli.bmp")
        imgMaster = imgMaster.convert()
        
        self.imgList = []
        
        imgSize = (128, 64)
        offset = ((2, 78), (134, 78), (266, 78), (398, 78))

        for i in range(4):
            tmpImg = pygame.Surface(imgSize)
            tmpImg.blit(imgMaster, (0, 0), (offset[i], imgSize))
            transColor = tmpImg.get_at((1, 1))
            tmpImg.set_colorkey(transColor)
            self.imgList.append(tmpImg)
    
    def update(self):
        self.pause += 1
        if self.pause >= self.delay:
            self.pause = 0
            self.frame += 1
            if self.frame >= len(self.imgList):
                self.frame = 0
                
            self.image = self.imgList[self.frame]
            self.rect = self.image.get_rect()
            self.rect.center = (320, 240)

def main():
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Using a multi-image master file")
    
    background = pygame.Surface(screen.get_size())
    background.fill((0x99, 0x99, 0xFF))
    screen.blit(background, (0, 0))
    
    chopper = Chopper()
    allSprites = pygame.sprite.Group(chopper)
    
    clock = pygame.time.Clock()
    keepGoing = True
    
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
        
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
        
        pygame.display.flip()
        
if __name__ == "__main__":
    main()