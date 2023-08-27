import pygame
import sys

# Farben
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialisierung
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dialog mit Pygame")

font = pygame.font.Font(None, 28)


def show_dialog():
    dialog_text = ""
    input_text = ""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    dialog_text += "Benutzer: " + input_text + "\n"
                    input_text = ""
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

        screen.fill(WHITE)

        # Zeige den Dialogverlauf an
        dialog_surface = font.render(dialog_text, True, BLACK)
        screen.blit(dialog_surface, (20, 20))

        # Zeige das Eingabefeld an
        input_surface = font.render("Eingabe: " + input_text, True, BLACK)
        screen.blit(input_surface, (20, height - 40))

        pygame.display.flip()


# Hauptprogramm
show_dialog()
