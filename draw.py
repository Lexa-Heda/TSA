from main import *


class Draw_handler:
    def __init__(self, screen):
        self.screen = screen
        self.to_draw = []

    def main(self):
        for element in self.to_draw:
            self.screen.blit(element.image, element.pos)


        self.draw_character()

    def draw_character(self):  # , pos, frame):
        # self.pos = pos
        pass
