from circleshape import CircleShape
import pygame
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y,radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)

    def update(self, dt):

        self.position += self.velocity * dt
    
    def split(self,):
        
        #destory it self
        self.kill()

        #min thresh hold to split
        if self.radius <= ASTEROID_MIN_RADIUS:
            return "this was a small asteroid"
        
        rand_angle = random.uniform(20,50)

        velocity_one = self.velocity.rotate(rand_angle)
        velocity_two = self.velocity.rotate(-rand_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        #create two new astroids
        aster1 = Asteroid(self.position.x,self.position.y,new_radius)
        aster2 = Asteroid(self.position.x,self.position.y,new_radius)
        aster1.velocity = velocity_one * 1.2
        aster2.velocity = velocity_two * 1.2