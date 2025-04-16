from random import randrange

from pygame_widgets.textbox import TextBox
import pygame_widgets
from pygame_widgets.slider import Slider

from boid import Boid
import pygame
import utils

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption('Boids Simulation')
clock = pygame.time.Clock()
running = True

font = pygame.font.Font('freesansbold.ttf', 18)

text_1 = font.render('Max Speed', True, "white")
text_2 = font.render('Min Speed', True, "white")
text_3 = font.render('Protected Range', True, "white")
text_4 = font.render('Visible Range', True, "white")
text_5 = font.render('Number of Boids', True, "white")
text_6 = font.render('Turn Factor', True, "white")
text_7 = font.render('Avoid Factor', True, "white")
text_8 = font.render('Matching Factor', True, "white")
text_9 = font.render('Centering Factor', True, "white")

rect_1 = text_1.get_rect()
rect_2 = text_2.get_rect()
rect_3 = text_3.get_rect()
rect_4 = text_4.get_rect()
rect_5 = text_5.get_rect()
rect_6 = text_6.get_rect()
rect_7 = text_7.get_rect()
rect_8 = text_8.get_rect()
rect_9 = text_9.get_rect()

# 60
rect_1.left = 10
rect_1.top = 10

rect_2.left = 10
rect_2.top = 70

rect_3.left = 10
rect_3.top = 130

rect_4.left = 10
rect_4.top = 190

rect_5.left = 10
rect_5.top = 250

rect_6.left = 10
rect_6.top = 310

rect_7.left = 10
rect_7.top = 370

rect_8.left = 10
rect_8.top = 430

rect_9.left = 10
rect_9.top = 490

output_1 = TextBox(screen, 130, 38, 30, 25, fontSize=15)
max_speed = Slider(screen, 20, 40, 80, 20, min=1, max=8, step=1, initial=utils.max_speed, handleColour=(128, 128, 128))

output_2 = TextBox(screen, 130, 98, 30, 25, fontSize=15)
min_speed = Slider(screen, 20, 100, 80, 20, min=-8, max=1, step=1, initial=utils.min_speed, handleColour=(128, 128, 128))

output_3 = TextBox(screen, 130, 158, 30, 25, fontSize=15)
protected_range = Slider(screen, 20, 160, 80, 20, min=5, max=20, step=1, initial=utils.protected_range, handleColour=(128, 128, 128))

output_4 = TextBox(screen, 130, 218, 30, 25, fontSize=15)
visible_range = Slider(screen, 20, 220, 80, 20, min=20, max=100, step=1, initial=utils.visible_range, handleColour=(128, 128, 128))

output_5 = TextBox(screen, 130, 278, 35, 25, fontSize=15)
num_boids = Slider(screen, 20, 280, 80, 20, min=5, max=200, step=1, initial=150, handleColour=(128, 128, 128))

output_6 = TextBox(screen, 130, 338, 30, 25, fontSize=15)
turn_factor = Slider(screen, 20, 340, 80, 20, min=0.1, max=1, step=0.1, initial=utils.turn_factor, handleColour=(128, 128, 128))

output_7 = TextBox(screen, 130, 398, 30, 25, fontSize=15)
avoid_factor = Slider(screen, 20, 400, 80, 20, min=0.1, max=1, step=0.1, initial=utils.avoid_factor, handleColour=(128, 128, 128))

output_8 = TextBox(screen, 130, 458, 40, 25, fontSize=15)
matching_factor = Slider(screen, 20, 460, 80, 20, min=0.01, max=0.1, step=0.01, initial=utils.matching_factor, handleColour=(128, 128, 128))

output_9 = TextBox(screen, 130, 518, 55, 25, fontSize=15)
centering_factor = Slider(screen, 20, 520, 80, 20, min=0.0001, max=0.001, step=0.0001, initial=utils.centering_factor, handleColour=(128, 128, 128))

boids = [Boid(randrange(0, utils.screen_width), randrange(0, utils.screen_height), randrange(utils.min_speed, utils.max_speed), randrange(utils.min_speed, utils.max_speed), 3, "cyan") for _ in range(150)]

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
        b.draw()


    v1 = max_speed.getValue()
    output_1.setText(v1)
    utils.max_speed = v1

    v2 = min_speed.getValue()
    output_2.setText(v2)
    utils.min_speed = v2

    v3 = protected_range.getValue()
    output_3.setText(v3)
    utils.protected_range = v3

    v4 = visible_range.getValue()
    output_4.setText(v4)
    utils.visible_range = v4

    v5 = num_boids.getValue()
    output_5.setText(v5)
    while len(boids) < v5:
        boids.append(Boid(randrange(0, utils.screen_width), randrange(0, utils.screen_height), randrange(utils.min_speed, utils.max_speed), randrange(utils.min_speed, utils.max_speed), 3, "cyan"))

    while len(boids) > v5:
        boids.pop()

    v6 = turn_factor.getValue()
    output_6.setText(v6)
    utils.turn_factor = v6

    v7 = avoid_factor.getValue()
    output_7.setText(v7)
    utils.avoid_factor = v7

    v8 = matching_factor.getValue()
    output_8.setText(v8)
    utils.matching_factor = v8

    v9 = centering_factor.getValue()
    output_9.setText(v9)
    utils.centering_factor = v9

    screen.blit(text_1, rect_1)
    screen.blit(text_2, rect_2)
    screen.blit(text_3, rect_3)
    screen.blit(text_4, rect_4)
    screen.blit(text_5, rect_5)
    screen.blit(text_6, rect_6)
    screen.blit(text_7, rect_7)
    screen.blit(text_8, rect_8)
    screen.blit(text_9, rect_9)

    pygame_widgets.update(event)
    pygame.display.update()


    # flip() the display to put your work on screen
    pygame.display.flip()
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()