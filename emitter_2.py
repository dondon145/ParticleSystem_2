import particle
import random


BLUE = (0, 0, 255)
RED = (255, 0, 0)
class Emitter_2 :

    def get_particles(self):
        self.particle_pool.append([particle.RectangularParticle(400, 400, BLUE, 10, 10, 0, 90, 10, 2, 1), "alive"])
        self.particle_pool.append([particle.RectangularParticle(400, 400, RED, 10, 10, 0, 120, 10, 2, 1), "alive"])

        
    def check_emission_status(self):
        return self.emission_status
    
    def set_requested_particle_amount(self, val):
        self.requested_particle_amount = val
    
    def check_requested_particle_amount(self):
        return self.requested_particle_amount
    
    def check_life_status(self, index_value):
        if self.particle_pool[index_value][0].get_life_val() < 0:
            self.particle_pool[index_value][1] = "dead"
            self.particle_pool[index_value][0]

    def switch_index_by_life_status(self):
        # if the particle is dead, we will look for the particle that is alive and switch their indexes 

        for i in range(len(self.particle_pool)):
            if self.particle_pool[i][1] == "dead":
                for b in range(len(self.particle_pool)):
                    if self.particle_pool[b][1] == "alive":
                        if i < b:
                            self.particle_pool[i], self.particle_pool[b] = self.particle_pool[b], self.particle_pool[i]
    
    def check_available_particle_amount(self):
        available = 0

        for i in range(len(self.particle_pool)):
            if self.particle_pool[i][1] == "alive":
                available +=1
        
        return available
    
    def compare_requested_to_available(self):
        # if there is not enough particles, then we will you the amount that is available to us
        available = self.check_available_particle_amount()
        if self.requested_particle_amount > available:
            self.set_requested_particle_amount(available)


    def emitt(self):
        for i in range(self.requested_particle_amount):
            self.group.add(self.particle_pool[i][0])


    
    def revive(self, index_value):
        if self.particle_pool[index_value][1] == 'dead':
            self.particle_pool[index_value][0].set_life_val(1.5)
            self.particle_pool[index_value][1] = 'alive'
            print("reviving", self.particle_pool[index_value][0].get_life_val())
            self.particle_pool[index_value][0].set_initial_position(400, 400)
            self.particle_pool[index_value][0].set_initial_time(0)
            self.particle_pool[index_value][0].set_velocity_to_initial()
            #print(self.particle_pool[0][0].get_life_val(), self.particle_pool[0][1], self.particle_pool[0][0].pos_y)
    
    def update(self):
        if self.emission_status == True:



    def __init__(self, amount, group):
        self.particle_pool = []
        self.group = group
        self.amount = amount

        self.emission_status = False
        self.requested_particle_amount = 0

        self.get_particles()

    

        