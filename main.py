import pygame
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

    # set player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        
        _ = screen.fill(bg_color)
        player.draw(screen)

        pygame.display.flip()

        tick = clock.tick(60)
        dt = tick/1000



if __name__ == "__main__":
    main()
