import pygame
from constants import *

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collision(self,circle):
        
        distance = pygame.Vector2.distance_to(self.position, circle.position)

        if self.radius + circle.radius > distance:
            return True
        else:
            return False
    
    def Boundary(position):
        if position.x > SCREEN_WIDTH:
            position.x = 1
        elif position.x < 0:
            position.x = SCREEN_WIDTH -1
        
        if position.y > SCREEN_HEIGHT:
            position.y = 1
        elif position.y < 0:
            position.y = SCREEN_HEIGHT -1
        
        return position