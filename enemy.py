from main import *


class Enemy:
    def __init__(self, leben, level):
        self.max_health = leben
        self.current_health = leben

        self.level = level