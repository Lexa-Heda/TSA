import pygame.mouse

import main


class Button:
    def __init__(self, image, pos, command_code, scale=1):
        self.code = command_code
        self.image_path = image
        self.image = pygame.image.load(image)
        self.image_size = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (self.image_size[0] * scale, self.image_size[1] * scale))
        self.rect = self.image.get_rect(topleft=pos)
        self.image_size = (self.image_size[0] * scale, self.image_size[1] * scale)


    def button_mouseover(self):
        # für farbänderung
        mouse = pygame.mouse.get_pos()
        if self.rect[0] <= mouse[0] <= self.rect[0] + self.rect[0] and self.rect[1] <= mouse[1] <= self.rect[1] + self.rect[1]:
            return True

    def button_mouseclick(self, maus):
        if pygame.mouse.get_pressed()[0]:
            mouse = maus
            if self.rect[0] <= mouse[0] <= self.rect[0] + self.rect[0] and self.rect[1] <= mouse[1] <= self.rect[1] + self.rect[1]:
                return True

    def run_command(self):
        exec(self.code)

