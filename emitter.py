
import particle
import random
import pygame

# colors 
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (128, 128, 0)


class Emitter():
    
    
    def sort_pool(self):
        # it moves the used particle in the end of the particle pool, and deletes it from previous index point
        for i in range(len(self.particle_pool)):
            if self.particle_pool[i][1] == 'in use':
                self.particle_pool.append(self.particle_pool[i])
                del self.particle_pool[i]

    # should be called if certain event met
    # otherwise might malfunction
    def emitt(self, use_ammount, group):
        for i in range(use_ammount):
            group.add(self.particle_pool[i][0])
            self.particle_pool[i][1] = "in use"

    def update(self):
        self.sort_pool()

    def __init__(self, amount, group):
        self.particle_pool = []
        self.group = group

        # particle values
        self.pos_x = 400
        self.pos_y = 400
        self.color = BLUE
        self.speed = 25
        self.gravity = 1

        for i in range(amount):
            width = random.randrange(25, 31)
            height = random.randrange(25, 31)
            angle_x = random.randrange(87, 92)
            angle_y = random.randrange(87, 92)
            life = random.randrange(1, 3)

            self.obj = particle.RectangularParticle(self.pos_x, self.pos_y, self.color, width, height, angle_x, angle_y, self.speed, self.gravity, life)
            self.particle_pool.append([self.obj, 'not in use'])


moving_particles = pygame.sprite.Group()
obj_1 = Emitter(10, moving_particles)
for i in range(len(obj_1.particle_pool)):
    print(f"particle {i} : ", obj_1.particle_pool[i])
    