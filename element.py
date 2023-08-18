from main import *
import pygame


class Element:
    # Container für daten
    def __init__(self, image_path, pos, animation=False, scale=1, rect_point="topleft"):
        self.image_path = image_path
        self.scale = scale
        self.frame = 0
        if not animation:
            self.image = pygame.image.load(self.image_path)
            self.size = self.image.get_size()
            self.image = pygame.transform.scale_by(self.image, scale)
        else:
            self.image = pygame.image.load(self.image_path + str(self.frame) + ".png")
            self.size = self.image.get_size()
            self.image = pygame.transform.scale_by(self.image, scale)

        self.bool_animate = animation

        # Ja dass mussso kompliziert für rect points!
        # Auch wenn wir die meisten eh nie brauchen werden...
        # Nico: Total unnötig!!!...
        if rect_point == "topleft":
            self.rect = self.image.get_rect(topleft=pos)
        elif rect_point == "center":
            self.rect = self.image.get_rect(center=pos)
        elif rect_point == "midleft":
            self.rect = self.image.get_rect(midleft=pos)
        elif rect_point == "bottomleft":
            self.rect = self.image.get_rect(bottomleft=pos)
        elif rect_point == "midbottom":
            self.rect = self.image.get_rect(midbottom=pos)
        elif rect_point == "bottomright":
            self.rect = self.image.get_rect(bottomright=pos)
        elif rect_point == "midright":
            self.rect = self.image.get_rect(midright=pos)
        elif rect_point == "topright":
            self.rect = self.image.get_rect(topleft=pos)
        elif rect_point == "midtop":
            self.rect = self.image.get_rect(midtop=pos)

        # Ab jetzt ist wida normaler Code
        # Schau mal ob ich nicht ausversehen bool_animate kaputt gemacht habe
        # also das oben Zeile 17 ca.
        if not not self.bool_animate:
            self.frame_timer = Timer(pygame.time.get_ticks(), 500)
            self.frame = 0

    def update(self):
        if self.bool_animate:
            if self.frame_timer.update():
                self.frame += 1
                self.frame_timer = Timer(pygame.time.get_ticks(), 500)
                if self.frame >= 4:
                    self.frame = 0
            self.animate(self.frame)

    def animate(self, frame):
        frame = frame
        self.image = pygame.image.load(self.image_path + "/" + str(frame) + ".png")
        self.image = pygame.transform.scale_by(self.image, self.scale)

