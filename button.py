import pygame.mouse

import main


class Button:
    def __init__(self, image, pos, command_code):
        self.code = command_code
        self.image_path = image
        self.image = pygame.image.load(image)
        self.image_size = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (self.image_size[0] * 4, self.image_size[1] * 4))
        self.rect = self.image.get_rect(topleft=pos)


    def button_mouseover(self):
        # für farbänderung
        mouse = pygame.mouse.get_pos()
        if self.pos[0] <= mouse[0] <= self.rect[0] + self.rect[0] and self.rect[1] <= mouse[1] <= self.rect[1] + self.rect[1]:
            return True

    def button_mouseclick(self, maus):
        if pygame.mouse.get_pressed()[0]:
            mouse = maus
            if self.pos[0] <= mouse[0] <= self.rect[0] + self.rect[0] and self.rect[1] <= mouse[1] <= self.rect[1] + self.rect[1]:
                return True

    def run_command(self):
        exec(self.code)

