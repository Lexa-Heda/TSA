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
        self.to_draw = []

    def update(self):
        # alle sachen zeichnen
        for element in self.to_draw:
            element.image = pygame.transform.scale(element.image, (element.size[0] * 4, element.size[1] * 4))
            self.screen.blit(element.image, element.pos)

class Button_handler:
    def __init__(self, screen):
        self.screen = screen
        self.buttons = []
    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        for button in self.buttons:
            if button.button_mouseclick(mouse_pos):
                button.run_command()

