import pygame
from main import *
from save_client import *
import sys


class Dialog:
    def __init__(self, draw_handler, font):
        self.font = font
        self.draw_handler = draw_handler
        self.rect = (100, 100)
        self.image = self.font.render("Username: ", True, (255, 255, 255))
        self.input_text = "Test"
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ENT:
                    out = self.input_text
                    client("save_data", out)
                    self.draw_handler.to_draw.clear()
                elif event.key == pygame.K_BACKSPACE:
                    self.input_text = self.input_text[:-1]
                    print("Erase")
                else:
                    self.input_text.join(event.unicode)
        self.image = self.font.render("Username " + self.input_text, True, (255, 255, 255))


class Button:
    def __init__(self, image, pos, command_code, draw_handler, gui_handler=None, scale=1, rect_point="topleft", image_mouseover=None, btn_handler=None):
        pygame.font.init()
        self.code = command_code
        self.btn_handler = btn_handler
        self.image_path = image
        self.image_path_mouseover = image_mouseover
        self.image = pygame.image.load(image)
        self.gui_handler = gui_handler

        self.font = pygame.font.Font("graphics/font.ttf", 36)
        self.input_username = ""


        self.data_to_store_data = [10]

        self.screen_state = "self.create_main_menu()"
        self.screen_state_changed = False

        self.image_size = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (self.image_size[0] * scale, self.image_size[1] * scale))


        self.draw_handler = draw_handler

        # rect Einstellungen
        if True:
            if rect_point == "topleft":
                self.rect = self.image.get_rect(topleft=pos)
            elif rect_point == "center":
                self.rect = self.image.get_rect(center=pos)
            elif rect_point == "midleft":
                self.rect = self.image.get_rect(midleft=pos)
            elif rect_point == "bottomleft":
                self.rect = self.image.get_rect(bottomleft=pos)
            elif rect_point == "midbottom":
                self.rect = self.image.get_rect(midbottom=pos)
            elif rect_point == "bottomright":
                self.rect = self.image.get_rect(bottomright=pos)
            elif rect_point == "midright":
                self.rect = self.image.get_rect(midright=pos)
            elif rect_point == "topright":
                self.rect = self.image.get_rect(topleft=pos)
            elif rect_point == "midtop":
                self.rect = self.image.get_rect(midtop=pos)

        self.image_size = (self.image_size[0] * scale, self.image_size[1] * scale)


    def button_mouseover(self):
        # für die Farbänderung
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            return True


    def prepare_next_screen(self):
        # Also wenn sich der Bildschirmstatus (Base, main_menu...) geändert hat...
        if self.screen_state_changed:
            # ... dann mache das da auf False, damit das nicht jeden Tick ausgeführt wird
            self.screen_state_changed = False

            # sowie alles leeren damit nicht auch die alten sachen angezeigt werden
            self.draw_handler.to_draw.clear()
            self.btn_handler.buttons.clear()

            # ...und dann mache den screen state auf den hier gespeicherten (siehe line 11) in diesem script
            exec(self.screen_state)

    def button_mouseclick(self, maus):
        # um die Commands auszuführen wenn auf den Button geklickt wird
        if pygame.mouse.get_pressed()[0]:
            mouse_pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(mouse_pos):
                return True

    def show_dialog(self):
        self.draw_handler.to_draw.append(Dialog(self.draw_handler, self.font))

    def save_data(self):
        self.btn_handler.clear_screen()
        self.show_dialog()




    def run_command(self):
        global out
        exec(self.code)
