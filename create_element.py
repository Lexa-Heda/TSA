from main import *
from handler import *
import pygame, sys
from element import *


class Create_GUI:
    def __init__(self, drawhandler, buttonhandler):
        self.handler = drawhandler
        self.btn_handler = buttonhandler

    def create_main_menu(self):
        # Jedes "if True:"ist die Abgrenzung eines grafischen Elementes
        if True:
            image_path = "graphics/png/buttons/start_button.png"
            self.handler.to_draw.append(Element(image_path, (100, 99), scale=8))
            self.btn_handler.buttons.append(Button(image_path, (100, 100), "self.btn_handler.clear_screen()", self.btn_handler, scale=8))
        if True:
            # Stuff um das Lagerfuer mittig zu machen...
            self.handler.to_draw.append(Element("graphics/png/objekts/campfire/", (640, 360), True, scale=6))
        if True:
            image_path = "graphics/png/buttons/exit_button.png"
            self.handler.to_draw.append(Element(image_path, (500, 500), scale=8))
            self.btn_handler.buttons.append(Button(image_path, (500, 500), "sys.exit()", self.btn_handler, scale=8))


