import pygame, sys
import time
import threading


class Main():
    def __init__(self):
        self.screen = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)

    def gameloop(self):
        while True:
            for event in pygame.event.get():
                if event == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    def run(self):
        self.gameloop()



if __name__ == "__main__":
    main = Main()
    main.run()
