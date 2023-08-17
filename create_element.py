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
            image_path = "graphics/png/buttons/start_button.png"
            self.handler.to_draw.append(Element(image_path, (100, 99), scale=8))
            self.btn_handler.buttons.append(Button(image_path, (100, 100), "pygame.quit()", scale=8))
        if True:
            self.handler.to_draw.append(Element("graphics/png/objekts/campfire/", (200, 200), True, scale=6))
