
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
        for i in range(len(self.particle_pool)):
            
            if self.particle_pool[i][1] == 'in use':
                print("sorting_1")
                if self.particle_pool[i][0].get_life_val() < 0:
                    print("SORTING_2")
                    for b in range(len(self.particle_pool), -1, -1):
                        if self.particle_pool[b][1] == 'not in use':
                            return b
                    self.particle_pool[i][0].set_life_val(3)
                    self.particle_pool[i][1] = 'not in use'
                    self.particle_pool[b][1] = 'in use'
                    self.particle_pool[i], self.particle_pool[b] = self.particle_pool[b], self.particle_pool[i]
    

    
   

    # should be called if certain event met
    # otherwise might malfunction
    def emitt(self, use_ammount, group):
        for i in range(len(self.particle_pool)):
            if self.particle_pool[i][0].get_life < 0 :
                print("life is not not zero")
                if self.particle_pool[i][1] == "not in use":
                    pass


    def add_to_group(self, group):
        for i in range(len(self.particle_pool)):
            group.add(self.particle_pool[i][0])

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


    """def sort_pool(self):
        # it moves the used particle in the end of the particle pool, and deletes it from previous index point
        for i in range(len(self.particle_pool)):
            if self.particle_pool[i][1] == 'in use':
                self.particle_pool.append(self.particle_pool[i])
                del self.particle_pool[i]

            if self.particle_pool[i][0].life < 0 :
                self.particle_pool.insert(0, self.particle_pool[i])
                self.particle_pool[0][1] = 'not in use'
                self.particle_pool[0].kill()
                self.particle_pool[0][0].life = 3
                del self.particle_pool[i]"""
    