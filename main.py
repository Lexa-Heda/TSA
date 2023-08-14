import pygame, sys
import time
import threading
from draw import *
from element import *



class Main:
    def __init__(self):
        self.screen = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
        self.draw = Draw_handler(self.screen)
        #self.

    def gameloop(self):
        while True:
            for event in pygame.event.get():
                if event == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.draw.main()
            self.screen.fill((0, 0, 0))

    def run(self):
        self.gameloop()


if __name__ == "__main__":
    main = Main()
    main.run()

#Netbook
# Dies ist vom netbook aus gemacht worden