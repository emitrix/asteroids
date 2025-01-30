# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    #Initialize the game
    print (f"Starting asteroids!")
    pygame.init()
    fpsClock = pygame.time.Clock()
    dt = 0
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Goups
    updatable  = pygame.sprite.Group()
    drawable   = pygame.sprite.Group()
    asteroids   = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    
    #player
    player_one = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    asteroid_field = AsteroidField()
    
    # Game Loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = 0
                return
        dt = fpsClock.tick(60) / 1000
        screen.fill(COLOR_BLACK)
        
        for thing in updatable:
            thing.update(dt)
        for thing in drawable:
            thing.draw(screen)
        
        pygame.display.flip()
        
    pygame.quit()


if __name__ == "__main__":
    main()
