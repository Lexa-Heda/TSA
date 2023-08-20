from main import *


class Enemy:
    def __init__(self, leben, level, name):
        self.max_health = leben
        self.current_health = leben
        self.name = name
        self.level = level


# Was soll das?
enemys = [Enemy(10, 1, "Goblin")]
