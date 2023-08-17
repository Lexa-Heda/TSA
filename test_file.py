import sys

import pygame

screen = pygame.display.set_mode((800, 600))

image = pygame.image.load("graphics/" + "png/buttons/start_button.png")

image = pygame.transform.scale(image, (320, 160))

while True:

    for event in pygame.event.get():
        keys = pygame.key.get_pressed()

        if keys[pygame.K_e]:
            pygame.quit()
            sys.exit()

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))
    screen.blit(image, (100, 100))
    pygame.display.update()
