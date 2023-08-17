import pygame.mouse

from main import *
from create_element import *
from button import *

class Draw_handler:
    def __init__(self, screen):
        self.screen = screen
        self.to_draw = []

    def update(self):
        # alle sachen zeichnen
        for element in self.to_draw:
            self.screen.blit(element.image, element.rect)

class Button_handler:
    def __init__(self, screen):
        self.screen = screen
        self.buttons = []
    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        for button in self.buttons:
            if button.button_mouseclick(mouse_pos):
                # alle button Funktionen auflisten
                pass
