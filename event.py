from main import *

class Event:
    def __init__(self, name, type, draw_handler):

        self.event_name = name
        self.event_type = type

        self.draw_handler = draw_handler


    def activate(self):
        if self.event_type == "fight":
            enemy = Enemy(10, 1, self.event_name)

            self.system = Fight_System(self.draw_handler, enemy, None)
            #


    def update_texts(self):
        self.system.update_text()
