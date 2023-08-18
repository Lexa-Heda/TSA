import pygame

from main import *

class Fight_System:
    def __init__(self, current_enemy, player):
        pygame.font.init()

        self.font = pygame.font.Font("graphics/font.ttf", 36)
        self.enemy = current_enemy
        self.player = player

        self.textphrase1 = f"Ein/e {current_enemy.name}"



    def fight(self):
        if self.player.level > self.enemy.level:
            self.player.level += 1
            self.winner = "Player"



