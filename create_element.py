from main import *
from handler import *
import pygame, sys
from element import *


class Create_GUI:
    def __init__(self, drawhandler, buttonhandler):
        self.handler = drawhandler
        self.btn_handler = buttonhandler

    def create_main_menu(self):
        # Jedes "if True: "ist die Abgrenzung eines grafischen Elementes
        if True:
            pass
            # background
            #self.handler.to_draw.append(Element("graphics/png/backgrounds/main_menu_background.png", (0, 0), scale=80))
        if True:
            # start button
            image_path = "graphics/png/buttons/start_button.png"
            image_pos = (640, 610)
            self.handler.to_draw.append(Element(image_path, image_pos, scale=6, rect_point="midbottom"))
            self.btn_handler.buttons.append(Button(image_path, image_pos, "self.btn_handler.clear_screen()", self.btn_handler, scale=6, rect_point="midbottom"))
        if True:
            # campfire
            self.handler.to_draw.append(Element("graphics/png/objekts/campfire/", (640, 500), True, scale=4, rect_point="bottomright"))
        if True:
            # exit button
            image_path = "graphics/png/buttons/exit_button.png"
            image_pos = (640, 715)
            self.handler.to_draw.append(Element(image_path, image_pos, scale=6, rect_point="midbottom"))
            self.btn_handler.buttons.append(Button(image_path, image_pos, "sys.exit()", self.btn_handler, scale=6, rect_point="midbottom"))
        if True:
            # player
            self.handler.to_draw.append(Element("graphics/png/character/player/stand.png", (640, 500), scale=8, rect_point="bottomleft"))


