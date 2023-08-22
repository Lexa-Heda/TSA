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
        # Ist in Main() das Attribut self.screen
        self.screen = screen
        self.new_cursor = pygame.image.load("graphics/png/objekts/schwert_cursor1.png")
        self.to_draw = []


    # update() zeigt jedes graphische Element an und ruft die Funktion update() in der Klasse
    # Element auf, um das Bild von Objekten, welche animiert sind zu aktualisieren
    def update(self):
        # alle sachen zeichnen

        for element in self.to_draw:
            # das Bild von einem Button wird geändert wenn die maus auf ihm drauf ist
            if element.image_path_mouseover != None and element.button_handler:
                element.image_path = element.image_path_mouseover

            # aktualisiert das Bild wenn Animation und Timer ausgelaufen
            element.update()

            # Zeichnet das jetztige Element aus der Liste self.to_draw
            self.screen.blit(element.image, (element.rect[0], element.rect[1]))

        # um den Cursor anzuzeigen
        mouse_pos = pygame.mouse.get_pos()
        self.screen.blit(self.new_cursor, mouse_pos)


# Führt den Befehl eines Buttons aus, wenn dieser gedrückt wurde
# die Commands für die Buttons werden in create_element.py in der Klasse als string definiert
class Button_handler:
    def __init__(self, screen, draw_handler):
        self.screen = screen
        self.draw_handler = draw_handler
        self.buttons = []

    def click_update(self):
        mouse_pos = pygame.mouse.get_pos()
        for button in self.buttons:
            if button.button_mouseclick(mouse_pos):
                button.run_command()

    def mouseover_update(self):
        pass


    def clear_screen(self):
        self.buttons = []
        self.draw_handler.to_draw.clear()