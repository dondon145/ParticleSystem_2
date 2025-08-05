import pygame
from pygame.locals import *
import particle
import random
import emitter_3

pygame.init()

clock = pygame.time.Clock()
FPS = 60

DISPLAYWIDTH = 800
DISPLAYHEIGHT = 800

DISPLAY = pygame.display.set_mode((DISPLAYWIDTH, DISPLAYHEIGHT))

# colors 
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (128, 128, 0)

running = True


# particle values
pos_x = 400
pos_y = 400
color = RED
width = 30
height = 30
angle_x = 90
angle_y = 90
speed = 25
gravity = 1
life = 2


moving_group = pygame.sprite.Group()
obj = emitter_3.Emitter_3(moving_group)


while running:

    obj.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        
        if event.type == KEYDOWN:
            obj.set_emitter_active(True)

    DISPLAY.fill(BLACK)

    moving_group.update()
    moving_group.draw(DISPLAY)

    clock.tick(FPS)
    #print(moving_group)
    pygame.display.flip()