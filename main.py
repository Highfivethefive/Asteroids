import pygame
from constants import *

#init py game
pygame.init()

#GUI window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))




def main():

    #able to quit the program with X
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return


    running = True
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    while running:

        #each frame
        screen.fill("black")
        #render new frame
        pygame.display.flip() 








if __name__ == "__main__":
    main()