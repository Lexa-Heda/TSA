from main import *
from handler import *
import pygame
from element import *


class Create_GUI:
    def __init__(self, drawhandler):
        self.handler = drawhandler

    def create_base_menu(self):
        character_image = pygame.image.load("graphics/png/buttons/start_button.png")
        character_image = pygame.transform.scale_by(character_image, (6, 6))
        character_image_rect = character_image.get_rect(center = (640, 360))
        self.handler.to_draw.append(Element(character_image, character_image_rect))
