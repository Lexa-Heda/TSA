import sys
from saveDataManager import SaveDataManager
import pygame
import time
import threading
from create_element import *
from handler import *
from element import *


# Application
class Main:
    def __init__(self):
        self.screen = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()

        self.draw = Draw_handler(self.screen)
        self.btn_handler = Button_handler(self.screen)
        self.savemanager = SaveDataManager("saves/save.sv")
        self.savemanager.save_data([])
        self.GUI_setter = Create_GUI(self.draw, self.btn_handler)

    def gameloop(self):
        # Game loop
        pygame.mouse.set_visible(False)
        self.GUI_setter.create_base_menu()
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.fill((0, 0, 0))
            self.draw.update()
            self.btn_handler.update()
            pygame.display.update()
            self.clock.tick(60)

    def run(self):
        self.gameloop()


if __name__ == "__main__":
    # Application wird gestartet
    main = Main()
    main.run()
