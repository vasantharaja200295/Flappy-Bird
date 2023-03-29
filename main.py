import pygame
import sys
import random

def game_floor():
    screen.blit(floor_base, (floor_x_pos,900))

pygame.init()
clock = pygame.time.Clock()


screen = pygame.display.set_mode((570, 1024))


background = pygame.image.load('./assets/background.png').convert()
background = pygame.transform.scale2x(background)


bird = pygame.image.load('./assets/yellowbird-midflap.png').convert_alpha()
bird_rect = bird.get_rect(center=(100, 512))
bird = pygame.transform.scale2x(bird)

bird_y = 0
gravity = 0.1


floor_base = pygame.image.load('./assets/ground.png').convert()
floor_base = pygame.transform.scale2x(floor_base)
floor_x_pos = 0


while True:

    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_y = 0
                bird_y -= 0.01
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                bird_y = 0
                bird_y +=2

    bird_y += gravity
    bird_rect.centery += bird_y

    screen.blit(bird, bird_rect)

    floor_x_pos -= 1
    game_floor()
    if floor_x_pos <= -76:
        floor_x_pos = 0

    pygame.display.update()
    clock.tick(120)




