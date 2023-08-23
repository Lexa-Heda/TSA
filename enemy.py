

class Enemy:
    def __init__(self, leben, level, name):
        self.max_health = leben
        self.current_health = self.max_health
        self.name = name
        self.level = level
