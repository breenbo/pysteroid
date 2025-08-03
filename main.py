import pygame
from constants import *

def main():
    print("Starting Pysteroids!")

    #initialize the pygame module
    _ = pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # set FPS
    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        _ = screen.fill("black")
        pygame.display.flip()

        tick = clock.tick(60)
        dt = tick/1000



if __name__ == "__main__":
    main()
