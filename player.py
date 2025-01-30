import pygame
from circleshape import CircleShape
from constants import *


# Player class
class Player(CircleShape):
    def __init__(self, x, y, radius):
        # Call the base class constructor
        super().__init__(x, y,PLAYER_RADIUS)
        self.rotation = 0
    
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, COLOR_WHITE, self.triangle(),2)
        #return super().draw(screen)