import pygame
import time
pygame.init()
size = width,height = 640, 480

GROUND_HEIGHT = height-200
xPos = 0
yPos = 0

gameDisplay= pygame.display.set_mode(size)



class Dinosaur:
    dinocolour = 255,255,255
    DINOHEIGHT = 40
    DINOWIDTH = 20
    def __init__(self, surfaceHeight):
        self.x = 60
        self.y = 0
        self.yvelocity = 0
        self.height = self.DINOHEIGHT
        self.width = self.DINOWIDTH
        self.surfaceHeight = surfaceHeight
    def jump(self): 
        if(self.y == 0):
          self.yvelocity = 300
    def update(self, deltaTime): 
        self.yvelocity += -500*deltaTime #gravity
        self.y += self.yvelocity * deltaTime
        if self.y < 0: 
          self.y = 0
          self.yvelocity = 0

    def draw(self,display):
        pygame.draw.rect(display,dinocolour,[self.x,self.surfaceHeight-self.y-self.height,self.width,self.height])


def main():
    dino = Dinosaur(GROUND_HEIGHT)

    clock = pygame.time.Clock()
    while True:


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() #quits
                quit()
            if event.type == pygame.K_SPACE: 
                    dinosaur.jump() #Make dinosaur jump

        gameDisplay.fill((0,0,0))

        pygame.draw.rect(gameDisplay,(255,255,255), [30,30,40,50])
        pygame.draw.rect(gameDisplay,(255,255,255), [0,GROUND_HEIGHT, width, height-GROUND_HEIGHT])

main()


