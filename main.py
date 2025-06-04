import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
#init py game
pygame.init()

#GUI window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Asteroids")

#clock
clock = pygame.time.Clock()

#font for writing
font = pygame.font.SysFont("arial", 25)


def main():

    #variables
    dt = 0
    score = 0

    #groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Shot.containers = (shots,updatable,drawable)

    #group astroid
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)

    running = True
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    Player_1 = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

    asteroid_field = AsteroidField()
    
    while running:

        #able to quit the program with X
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) /1000

        #each frame
        screen.fill("black")

        #player update all things able to update
        updatable.update(dt)


        #check for collision and draw
        for astroid in asteroids:
            if Player_1.collision(astroid):
                print("Game over!")
                return
            
            #check if any bulley collides with astroid delete objects if they collide
            for bullet in shots:
                if bullet.collision(astroid):
                    astroid.split()
                    bullet.kill()

                    #calculate score when something gets destroyed
                    score +=  Asteroid.Score(astroid.radius)

            
            
        


        for obj in drawable:
            obj.draw(screen)

        #render text in bottom corner
        text = font.render(f"{score}", True, "white")
        screen.blit(text, [SCREEN_WIDTH - 60, SCREEN_HEIGHT - 30])

        #render new frame
        pygame.display.flip() 







if __name__ == "__main__":
    main()