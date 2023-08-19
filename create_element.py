from main import *
from handler import *
import pygame, sys
from element import *


class Create_GUI:
    def __init__(self, drawhandler, buttonhandler):
        self.handler = drawhandler
        self.btn_handler = buttonhandler

        self.screen_state = "self.create_main_menu()"
        self.screen_state_changed = False

    # Wird nur einmalig pro wechsel eines screens zum nächsten ausgeführt
    # Soll Draw_handler.to_draw leeren und die Funktion aufrufen, welche die Elemente des jetzigen screens in die to_draw Liste
    # einfügt
    def prepare_next_screen(self):
        # Also wenn sich der Bildschirmstatus (Base, main_menu...) geändert hat...
        if self.screen_state_changed:
            # ... dann mache das da auf False, damit das nicht jeden Tick ausgeführt wird
            self.screen_state_changed = False

            # sowie alles leeren damit nicht auch die alten sachen angezeigt werden
            self.Draw_handler.to_draw.clear()
            self.Button_handler.buttons.clear()

            # ...und dann mache den screen state auf den hier gespeicherten (siehe line 11) in diesem script
            exec(self.screen_state)

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

    def create_base(self):
        # Jedes "if True: "ist die Abgrenzung eines grafischen Elementes
        pass
