# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shoot import Shoot


def main():
    #Initialize the game
    print (f"Starting asteroids!")
    pygame.init()
    fpsClock = pygame.time.Clock()
    dt = 0
    game_score = 0
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Groups
    updatable, drawable, asteroids, shoots = [pygame.sprite.Group() for _ in range(4)]
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shoot.containers = (shoots, updatable, drawable)
    
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
        updatable.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collide(player_one) :
                print ("Player hit")
                print ("Game over!")
                print ("Score: ", game_score)
                running = False
                break
            for shoot in shoots:
                if asteroid.collide(shoot) :
                    asteroid.split()
                    shoot.kill()
                    game_score += 50
            
        screen.fill(COLOR_BLACK)
        
        for obj in drawable:
            obj.draw(screen)
       
        pygame.display.flip()
        
        #limit the frame rate to 60 fps
        dt = fpsClock.tick(60) / 1000
        
    pygame.quit()


if __name__ == "__main__":
    main()
