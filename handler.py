import pygame
import sys
from main import *
from create_element import *
from button import *


class Timer:
    def __init__(self, start_time, duration):
        self.start_time = start_time
        self.lenght = duration

    def update(self):
        self.current_time = pygame.time.get_ticks()
        self.elapsed_time = self.current_time - self.start_time
        if self.elapsed_time >= self.lenght:
            return True


class Draw_handler:
    def __init__(self, screen):
        self.screen = screen
        self.new_cursor = pygame.image.load("graphics/png/objekts/schwert_cursor1.png")
        self.to_draw = []

    def update(self):
        # alle sachen zeichnen

        for element in self.to_draw:
            self.screen.blit(element.image, (element.rect[0], element.rect[1]))
        mouse_pos = pygame.mouse.get_pos()
        self.screen.blit(self.new_cursor, mouse_pos)

# Führt den Befehl eines Buttons aus, wenn dieser gedrückt wurde
# die Commands für die Buttons werden in create_element.py in der Klasse
    def __init__(self, screen):
        self.screen = screen
        self.buttons = []

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        for button in self.buttons:
            if button.button_mouseclick(mouse_pos):
                button.run_command()

