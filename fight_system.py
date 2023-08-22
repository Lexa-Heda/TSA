import pygame
from main import *

class Fight_System:
    def __init__(self, draw_handler, current_enemy, player):
        pygame.font.init()

        self.enemys = [Enemy(10, 1, "Goblin")]

        self.draw_handler = draw_handler
        self.font = pygame.font.Font("graphics/font.ttf", 36)
        self.enemy = current_enemy
        self.player = player
        self.current_font = None

        self.text_active = False

        self.ein_eine = True

        if self.ein_eine:
            self.textphrase1 = f"Ein {current_enemy.name} erscheint und greift dich an!"
        else:
            self.textphrase1 = f"Eine {current_enemy.name} erscheint und greift dich an!"
        self.textphrase2 = f"Ihr bekämpft euch... die Spannung steigt... die Spannung steigt ins unermessliche..."
        self.textphrase3 = f"{self.winner} gewinnt!"
        self.current_text = f""

    def display_text(self):
        self.font = self.font.render(self.current_text, True, (255, 255, 255))
        self.draw_handler.to_draw.append(Element(self.font, (0, 0)))

    def update_text(self):
        if self.text_active:
            self.current_font


    def fight(self):
        if self.player.level >= self.enemy.level:
            self.player.level += 1
            self.winner = "player"
        else:
            self.winner = "enemy"



