from main import *
from handler import *
import pygame, sys
from element import *


class Create_GUI:
    def __init__(self, drawhandler, buttonhandler):
        self.handler = drawhandler
        self.btn_handler = buttonhandler

    def create_base_menu(self):
        if True:
            character_image = pygame.image.load("graphics/png/buttons/start_button.png")
            self.handler.to_draw.append(Element(character_image, (100, 99)))
            self.btn_handler.buttons.append(Button(character_image, (100, 100), "pygame.quit()"))
        if True:
            self.handler.to_draw.append(Element("graphics/png/objekts/campfire/", (200, 200), True))
