import pygame
from pygame.locals import *
import particle
import random

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

obj = particle.RectangularParticle(pos_x, pos_y, color, width, height, angle_x, angle_y, speed, gravity, life)
moving_group = pygame.sprite.Group()
moving_group.add(obj)

while running:

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    DISPLAY.fill(BLACK)

    moving_group.update()
    moving_group.draw(DISPLAY)
    clock.tick(FPS)
    pygame.display.flip()

for i in range(3):
    print(random.randrange(1, 4))