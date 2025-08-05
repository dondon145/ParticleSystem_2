import pygame
import particle

BLUE = (0, 0, 255)
RED = (255, 0, 0)

class Emitter_3 :
    def update(self):
        self.remove_all_dead_and_revive()
        self.no_alive_particles()

        
        #for i in range(len(self.particle_pool)):
         #   self.remove_dead(i)
        # always check if emitter is active
        # always check if particle pool has dead particles
        """
        - if it has dead particle then find the furthest index position that has a particle that is alive
        - switch the dead particle and alive particle by index positions in the particle pool
        - begin reviving a dead particle ( reset its life, reset its position, reset its velocity, reset its time)
        """
        # after the particle pool has been sorted out, find out how many particles are needed
        # check if particle pool has this much
        # if it has this much then emitt the amount that was asked
        # if the particle pool does not have this much particles then emitt all the particles that are alive

        if self.check_emitter_active()== True:
            self.emitt()


    def remove_all_dead_and_revive(self):
        for i in range(len(self.particle_pool)):
            self.remove_dead(i)
            self.revive(i)

    def remove_dead(self, index_value):
        if self.particle_pool[index_value][0].get_life_val() < 0:
            self.particle_pool[index_value][1] = "dead"
            self.group.remove(self.particle_pool[index_value][0])
    
    def count_alive_particles(self):
        alive_particles = 0
        for i in range(len(self.particle_pool)):
            if self.particle_pool[i][1] == "alive":
                alive_particles +=1 

        return alive_particles
    
    # stops the emitter from functioning if it has no particles available for work
    def no_alive_particles(self):
        alive_particles = self.count_alive_particles()
        if alive_particles < 1:
            self.set_emitter_active(False)
    
    def revive(self, index_value):
        if self.particle_pool[index_value][1] == 'dead':
            self.particle_pool[index_value][0].set_life_val(1.5)
            self.particle_pool[index_value][1] = 'alive'
            print("reviving", self.particle_pool[index_value][0].get_life_val())
            self.particle_pool[index_value][0].set_initial_position(400, 400)
            self.particle_pool[index_value][0].set_initial_time(0)
            self.particle_pool[index_value][0].set_velocity_to_initial()



    def get_particles(self):
        self.particle_pool.append([particle.RectangularParticle(400, 400, BLUE, 10, 10, 90, 120, 20, 1, 1), "alive"])
        self.particle_pool.append([particle.RectangularParticle(400, 400, RED, 10, 10, 90, 90, 20, 1, 1), "alive"])
        

    def check_emitter_active(self):
        return self.emitter_active
    
    def set_emitter_active(self, val):
        self.emitter_active = val
    
    def emitt(self):
        for i in range(len(self.particle_pool)):
            self.group.add(self.particle_pool[i][0])


    def __init__(self, group):
        self.group = group
        self.particle_pool = []
        self.emitter_active = False
        self.has_dead_particles = False

        self.get_particles()

    



    











    """
    def pool_has_dead_particles(self):
        return self.has_dead_particles 
    
    def scan_for_dead_and_alive_particles(self):
        dead_particle_index_list = []
        alive_particle_index_list = []
        for i in range(self.particle_pool):
            if self.particle_pool[i][1] == "dead":
                dead_particle_index_list.append(i)
            else :
                alive_particle_index_list.append(i)
            
        return dead_particle_index_list, alive_particle_index_list
    
    def sort_particle_pool(self):
        dead_particle_index_list, alive_particle_index_list = self.scan_for_dead_and_alive_particles()
        for i in range
    """
