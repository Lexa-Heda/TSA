import pygame

class Button:
    def __init__(self, image, pos, function_name):
        self.pos = pos
        self.image = image
        self.name = function_name
        self.size = self.image.get_size()

    def button_mouseover(self):
        mouse = pygame.mouse.get_pos()
        if self.pos[0] <= mouse[0] <= self.pos[0] + self.size[0] and self.pos[1] <= mouse[1] <= self.pos[1] + self.size[1]:
            return True

    def button_mouseclick(self):
        if pygame.mouse.get_pressed()[0]:
            mouse = pygame.mouse.get_pos()
            if self.pos[0] <= mouse[0] <= self.pos[0] + self.size[0] and self.pos[1] <= mouse[1] <= self.pos[1] + self.size[1]:
                return True
        return False