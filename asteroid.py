import pygame
from circleshape import CircleShape
from constants import *


# Player class
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        # Call the base class constructor
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen, COLOR_WHITE, self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
        