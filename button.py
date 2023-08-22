import pygame
from main import *



class Button:
    def __init__(self, image, pos, command_code, btn_handler, scale=1, rect_point="topleft", image_mouseover=None, gui=None):
        self.code = command_code
        self.btn_handler = btn_handler
        self.image_path = image
        self.gui = gui
        self.image_path_mouseover = image_mouseover
        self.image = pygame.image.load(image)
        self.image_size = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (self.image_size[0] * scale, self.image_size[1] * scale))

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

    def button_mouseclick(self, maus):
        # um die Commands auszuführen wenn auf den Button geklickt wird
        if pygame.mouse.get_pressed()[0]:
            mouse_pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(mouse_pos):
                return True

    def run_command(self):
        exec(self.code)
