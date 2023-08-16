import sys

import pygame

screen = pygame.display.set_mode((800, 600))


while True:

    for i in pygame.event.get():
        keys = pygame.key.get_pressed()

        if keys[pygame.K_e]:
            pygame.quit()
            sys.exit()

        if i.type == pygame.QUIT:
            print("0")

    screen.fill((0, 0, 0))
    screen.blit(pygame.image.load("graphics/png/buttons/start_button.png"), (100, 100))
    pygame.display.update()
