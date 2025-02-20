import pygame
from circleshape import CircleShape
from constants import *
from shoot import Shoot

# Player class
class Player(CircleShape):
    def __init__(self, x, y, radius):
        # Call the base class constructor
        super().__init__(x, y,PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_cooldown = 0
    
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
    
    def rotate(self, deltha):
        self.rotation += deltha * PLAYER_TURN_SPEED
        #self.rotation %= 360
    
    def update(self, dt):
        self.shoot_cooldown -= dt
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT] :
            self.rotate(-dt)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt)
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(dt)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
    
    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def shoot(self):
        if self.shoot_cooldown > 0:
            return
        self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN
        
        shoot = Shoot(self.position.x, self.position.y)
        shoot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        #print ("Shoot!")
        