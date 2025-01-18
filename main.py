import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def  main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroidfield = AsteroidField()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return     
        for sprite in updatable:
            sprite.update(dt)

        for asteroid in asteroids:
            if player.collision(asteroid):
                raise Exception("Game Over!")
        for asteroid in asteroids:
            for shot in shots:
                if shot.collision(asteroid):
                    asteroid.split()
                    shot.kill()
            
        screen.fill((0,0,0))

        for sprite in drawable:
            sprite.draw(screen)   

        pygame.display.flip()
        dt = clock.tick(60) / 1000
        fps = clock.get_fps()        

if __name__ == "__main__":
    main()