import pygame
from constants import *
from player import Player

#init py game
pygame.init()

#GUI window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#clock
clock = pygame.time.Clock()


def main():

    #variables
    dt = 0

    #able to quit the program with X
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return


    running = True
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    Player_1 = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

    while running:

        #each frame
        screen.fill("black")

        #player
        Player_1.draw(screen)
        #render new frame
        pygame.display.flip() 

        dt = clock.tick(60) /1000







if __name__ == "__main__":
    main()