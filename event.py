from main import *

class Event:
    def __init__(self, name, draw_handler):

        self.event_name = name
        self.draw_handler = draw_handler
    def activate(self):
        if self.event_name == "fight":
            enemy = Enemy(10, 1, "Goblin")
            self.system = Fight_System(self.draw_handler, enemy, None)
            #


    def update_texts(self):
        self.system.update_text()
