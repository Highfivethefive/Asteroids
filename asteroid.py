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
        #check boundray make sure it over laps
        #make a seperate one for circles
        ##self.position = CircleShape.Boundary(self.position)
    
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

        #create two new astroids and splits them in triangle type direction
        aster1 = Asteroid(self.position.x,self.position.y,new_radius)
        aster2 = Asteroid(self.position.x,self.position.y,new_radius)
        aster1.velocity = velocity_one * 1.2
        aster2.velocity = velocity_two * 1.2

    def Score(radius):
        if radius <= ASTEROID_MIN_RADIUS:
            score = 50
        elif radius >= ASTEROID_MIN_RADIUS * 2:
            score = 150
        else:
            score = 100
        return score
    
    def Player_Lives(lives,screen):
        
        if lives == 3:
            pygame.draw.polygon(screen, "white", [(SCREEN_WIDTH - 30, SCREEN_HEIGHT - 55), (SCREEN_WIDTH - 40, SCREEN_HEIGHT - 40), (SCREEN_WIDTH - 20, SCREEN_HEIGHT - 40)], 2)
            pygame.draw.polygon(screen, "white", [(SCREEN_WIDTH - 60, SCREEN_HEIGHT - 55), (SCREEN_WIDTH - 70, SCREEN_HEIGHT - 40), (SCREEN_WIDTH - 50, SCREEN_HEIGHT - 40)], 2)
            pygame.draw.polygon(screen, "white", [(SCREEN_WIDTH - 90, SCREEN_HEIGHT - 55), (SCREEN_WIDTH - 100,SCREEN_HEIGHT - 40), (SCREEN_WIDTH - 80, SCREEN_HEIGHT - 40)], 2)
        elif lives == 2:
            pygame.draw.polygon(screen, "white", [(SCREEN_WIDTH - 60, SCREEN_HEIGHT - 55), (SCREEN_WIDTH - 70, SCREEN_HEIGHT - 40), (SCREEN_WIDTH - 50, SCREEN_HEIGHT - 40)], 2)
            pygame.draw.polygon(screen, "white", [(SCREEN_WIDTH - 90, SCREEN_HEIGHT - 55), (SCREEN_WIDTH - 100,SCREEN_HEIGHT - 40), (SCREEN_WIDTH - 80, SCREEN_HEIGHT - 40)], 2)
        elif lives == 1:
            pygame.draw.polygon(screen, "white", [(SCREEN_WIDTH - 90, SCREEN_HEIGHT - 55), (SCREEN_WIDTH - 100,SCREEN_HEIGHT - 40), (SCREEN_WIDTH - 80, SCREEN_HEIGHT - 40)], 2)
        else:
            return
