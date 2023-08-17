from main import *
import pygame


class Element:
    # Container für daten
    def __init__(self, image_path, pos, animation=False, scale=1):
        self.image_path = image_path
        if not animation:
            self.image = pygame.image.load(self.image_path)
            self.size = self.image.get_size()
            self.image = pygame.transform.scale(self.image, (self.size[0] * 4, self.size[1] * 4))
        else:
            self.image = pygame.image.load(self.image_path + "0.png")
            self.size = self.image.get_size()


        self.rect = self.image.get_rect()
        self.bool_animate = animation

        if self.bool_animate:
            self.frame_timer = Timer(pygame.time.get_ticks(), 60)
            self.frame = 0

    def update(self):
        if self.bool_animate:
            if self.frame_timer.update():
                self.frame += 1
                if self.frame <= 4:
                    self.frame = 0
            self.animate(self.frame)

    def animate(self, frame):
        frame = frame
        self.image = pygame.image.load(self.image_path + "/" + str(frame) + ".png")


