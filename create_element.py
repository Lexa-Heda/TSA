from main import *
from handler import *
import pygame, sys
from element import *
import random

class Create_GUI:
    def __init__(self, drawhandler, buttonhandler, player):
        self.handler = drawhandler
        self.btn_handler = buttonhandler
        self.events = []
        self.screen_state = "self.create_main_menu()"
        self.screen_state_changed = False
        self.player = player

    # Wird nur einmalig pro wechsel eines screens zum nächsten ausgeführt
    # Soll Draw_handler.to_draw leeren und die Funktion aufrufen, welche die Elemente des jetzigen screens in die to_draw Liste
    # einfügt
    def prepare_next_screen(self):
        # Also wenn sich der Bildschirmstatus (Base, main_menu...) geändert hat...
        if self.screen_state_changed:
            # ... dann mache das da auf False, damit das nicht jeden Tick ausgeführt wird
            self.screen_state_changed = False

            # sowie alles leeren damit nicht auch die alten sachen angezeigt werden
            self.handler.to_draw.clear()
            self.btn_handler.buttons.clear()

            # ...und dann mache den screen state auf den hier gespeicherten (siehe line 11) in diesem script
            exec(self.screen_state)


    def choose_Event(self, true=True):
        r = random.randint(1, 50)
        event_type = None

        if true:
            if r == 1:
                event_type = "fight"
            else:
                self.choose_Event(True)
        else:
            r = random.randint(1, 50)
            if r == 1:
                return "goblin"
            else:
                self.choose_Event()
        return event_type



    def create_main_menu(self):
        # Jedes "if True: "ist die Abgrenzung eines grafischen Elementes
        if True:
            pass
            # background
            # self.handler.to_draw.append(Element("graphics/png/backgrounds/main_menu_background.png", (0, 0), scale=80))
        if True:
            # start button
            image_path = "graphics/png/buttons/start_button.png"
            image_pos = (640, 610)
            self.handler.to_draw.append(Element(self.btn_handler, image_path, image_pos, scale=6, rect_point="midbottom"))
            self.btn_handler.buttons.append(Button(image_path, image_pos, "self.btn_handler.clear_screen()\n\nself.gui_handler.create_base()", self.btn_handler, gui_handler=self, scale=6, rect_point="midbottom"))
        if True:
            # campfire
            self.handler.to_draw.append(Element(self.btn_handler, "graphics/png/objekts/campfire/", (640, 500), True, scale=4, rect_point="bottomright"))
        if True:
            # exit button
            image_path = "graphics/png/buttons/exit_button.png"
            image_pos = (640, 715)
            self.handler.to_draw.append(Element(self.btn_handler, image_path, image_pos, scale=6, rect_point="midbottom"))
            self.btn_handler.buttons.append(Button(image_path, image_pos, "sys.exit()", self.btn_handler, scale=6, rect_point="midbottom"))
        if True:
            # player
            self.handler.to_draw.append(Element(self.btn_handler, "graphics/png/character/player/stand.png", (640, 500), scale=8, rect_point="bottomleft"))
        if True:
            image_path = "graphics/png/buttons/save_button.png"
            image_pos = (640, 100)
            self.handler.to_draw.append(
                Element(self.btn_handler, image_path, image_pos, scale=6, rect_point="midbottom"))
            self.btn_handler.buttons.append(
                Button(image_path, image_pos, "print('Created new stuff')", self.btn_handler, scale=6, rect_point="midbottom"))

    def create_base(self):
        # Jedes "if True: "ist die Abgrenzung eines grafischen Elementes
        self.event = Event(self.choose_Event(True), self.handler, self.player)
        self.event.activate()
