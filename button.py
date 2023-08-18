import pygame
from main import *



class Button:
    def __init__(self, image, command_code, btn_handler, scale=1):
        self.code = command_code
        self.btn_handler = btn_handler
        self.image_path = image
        self.image = pygame.image.load(image)
        self.image_size = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (self.image_size[0] * scale, self.image_size[1] * scale))
        self.rect = self.image.get_rect(topleft=pos)
        self.image_size = (self.image_size[0] * scale, self.image_size[1] * scale)


    def button_mouseover(self):
        # für die Farbänderung
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            return True

    def button_mouseclick(self, maus):
        if pygame.mouse.get_pressed()[0]:
            mouse_pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(mouse_pos):
                return True

    def run_command(self):
        exec(self.code)
