import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player

def main():
    print("Starting Pysteroids!")

    #initialize the pygame module
    _ = pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    bg_color = "black"
    # bg_color = "white"

    # set FPS
    clock = pygame.time.Clock()
    dt = 0.0


    #groups: add Player class variable
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    # set player
    _ = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    _ = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        
        _ = screen.fill(bg_color)

        updatable.update(dt)
        # player.update(dt)
        # player.draw(screen)

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()

        tick = clock.tick(60)
        dt = tick/1000



if __name__ == "__main__":
    main()
