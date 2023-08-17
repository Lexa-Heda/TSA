import pygame.mouse

import main


class Button:
    def __init__(self, image, pos, command_code):
        self.pos = pos
        self.code = command_code
        self.image = image
        self.size = self.image.get_size()

    def button_mouseover(self):
        # für farbänderung
        mouse = pygame.mouse.get_pos()
        if self.pos[0] <= mouse[0] <= self.pos[0] + self.size[0] and self.pos[1] <= mouse[1] <= self.pos[1] + self.size[1]:
            return True

    def button_mouseclick(self, maus):
        if pygame.mouse.get_pressed()[0]:
            mouse = maus
            if self.pos[0] <= mouse[0] <= self.pos[0] + self.size[0] and self.pos[1] <= mouse[1] <= self.pos[1] + self.size[1]:
                return True

    def run_command(self):
        exec(self.code)

