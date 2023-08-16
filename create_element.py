from main import *
from draw import *

class Create_GUI:
    def __init__(self, handler):
        self.handler = handler

    def create_base_menu(self):
        character_image = pygame.image.load("graphics/png/buttons/start_button.png")
        self.handler.to_draw.append(Element(character_image, (100, 100)))


