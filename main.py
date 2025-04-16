from random import randrange
from boid import Boid
import pygame
import utils

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
running = True

boids = [Boid(randrange(0, screen.get_height()), randrange(0, screen.get_height()), randrange(utils.min_speed, utils.max_speed), randrange(utils.min_speed, utils.max_speed), 3, "cyan") for _ in range(50)]

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    screen.fill("black")

    for b in boids:
        b.update(boids)
        b.edges()
        b.draw()

    # flip() the display to put your work on screen
    pygame.display.flip()
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()