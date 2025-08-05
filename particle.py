import pygame
import math


class RectangularParticle(pygame.sprite.Sprite):

    def die(self):
        self.kill()

    def applied_gravity(self):
        if self.gravity != 0:
            self.gravity_applied = True

    def get_age_ratio(self):
        self.age_ratio = self.life/self.original_life

    def set_alpha(self):
        self.alpha = self.age_ratio

    def get_alpha(self):
        # alpha in pygame ranges from 0-255
        # we need to convert it to make it work
        return self.alpha* 255
    
    def set_initial_position(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
    
    def set_initial_time(self, time):
        self.time = time
    
    def set_position(self):

        if self.gravity_applied ==  True:
            self.vel_y += self.gravity* self.time

        self.pos_x += self.vel_x* self.time
        self.pos_y += self.vel_y* self.time

    def change_time(self, delta_time):
        self.time += delta_time
        self.life -= delta_time

    def set_rect_center(self):
        self.rect.center = (self.pos_x, self.pos_y)

    def get_life_val(self):
        return self.life
    
    def set_life_val(self, val):
        self.life = val

    def set_velocity_to_initial(self):
        self.vel_x = self.initial_vel_x
        self.vel_y = self.initial_vel_y

    def update(self):
        self.set_rect_center()
        self.change_time(1/60)
        self.get_age_ratio()
        self.set_alpha()
        self.image.set_alpha(self.get_alpha())
        self.set_position()


    def __init__(self, pos_x, pos_y, color, width, height, angle_x, angle_y, speed, gravity, life):
        super().__init__()
        self.image  = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)

        self.pos_x = pos_x
        self.pos_y = pos_y

        # might want to change angles in the future throughout program running
        # math module originally sticks to radians, so you need to convert to degrees if you want degrees
        self.initial_vel_x = self.vel_x = speed* math.cos(angle_x* math.pi/ 180)
        self.initial_vel_y = self.vel_y = -1* speed* math.sin(angle_y* math.pi/180)

        self.gravity = self.acceleration = gravity
        self.gravity_applied = False
        self.applied_gravity()

        self.original_life = self.life = life
        self.alpha = self.age_ratio = 1
        self.time = 0
