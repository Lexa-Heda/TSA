import pygame
from sys import exit
import time
import threading
from create_element import *
from draw import *
from element import *



class Main:
    def __init__(self):
        self.screen = pygame.display.set_mode((1280, 720))
        self.draw = Draw_handler(self.screen)

    def gameloop(self):
        # Game loop
        while True:
            # Event loop
            for event in pygame.event.get():
                if event == pygame.QUIT:
                    pygame.quit()
                    exit()
            self.screen.fill((0, 0, 0))
            self.draw.main()

    def run(self):
        self.gameloop()


if __name__ == "__main__":
    main = Main()
    main.run()

print("Alle Nuiggos schind dummsch")