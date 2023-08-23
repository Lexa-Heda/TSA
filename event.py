from main import *

class Event:
    def __init__(self, name, draw_handler, player):

        self.winner = None
        self.system = None
        self.event_name = name
        self.player = player
        self.draw_handler = draw_handler


    def activate(self):
        if self.event_name == "fight":
            enemy = Enemy(10, 1, self.event_name)

            self.system = Fight_System(self.draw_handler, enemy, self.player)
            self.winner = self.system.fight()
            print(self.winner)
            #


    def update_texts(self):
        self.system.update_text()
