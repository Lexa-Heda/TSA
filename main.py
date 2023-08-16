import sys

import pygame
import time
import threading
from create_element import *
from handler import *
from element import *


# App
class Main:
    def __init__(self):
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.draw = Draw_handler(self.screen)

        self.GUI_setter = Create_GUI(self.draw)


    def gameloop(self):
        # Game loop
        self.GUI_setter.create_base_menu()
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.fill((0, 0, 0))
            self.draw.update()
            pygame.display.update()
            self.clock.tick(60)

    def run(self):
        self.gameloop()


if __name__ == "__main__":
    # App wird gestartet
    main = Main()
    main.run()
