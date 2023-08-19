import pygame

from main import *

class Fight_System:
    def __init__(self, draw_handler, current_enemy, player):
        pygame.font.init()

        self.draw_handler = draw_handler
        self.font = pygame.font.Font("graphics/font.ttf", 36)
        self.enemy = current_enemy
        self.player = player
        self.current_font = None

        self.textphrase1 = f"Ein/e {current_enemy.name} erscheint und greift dich an!"
        self.textphrase2 = f"Ihr bekämpft euch..."
        self.textphrase3 = f"{self.winner} gewinnt!"


    def display_text(self):
        self.current_font = self.font.render(self.textphrase1, True, (255, 255, 255))
        self.draw_handler.to_draw.append(Element(self.current_font, (0, 0)))


    def fight(self):
        if self.player.level >= self.enemy.level:
            self.player.level += 1
            self.winner = "player"
        else:
            self.winner = "enemy"



