import pygame
from enemy import Enemy
from create_element import *
from handler import *
from fight_system import *


# Application
class Main:
    def __init__(self):

        # erstellt das Fenster mit 1280px * 720px und setzt es auf fullscreen
        self.screen = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)

        # Uhrenzeuch
        self.clock = pygame.time.Clock()

        # ja idk
        self.draw = Draw_handler(self.screen)
        self.btn_handler = Button_handler(self.screen, self.draw)
        self.GUI_setter = Create_GUI(self.draw, self.btn_handler)

        # Zum Speichern
        # self.savemanager = SaveDataManager("saves/save.sv")
        # self.savemanager.save_data([])

    def gameloop(self):

        # Game loop
        self.player = Enemy(10, 5, "player")

        pygame.mouse.set_visible(False)
        self.GUI_setter.create_main_menu()
        while True:
            self.GUI_setter.prepare_next_screen()

            # Event loop
            for event in pygame.event.get():
                # Wenn wech dann wech
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # wird nur ausgeführt wenn eine Maustaste gerade heruntergedrückt wurde
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Führt die Commands der Buttons aus, wenn dei linke Maustaste
                    # momentan gedrückt ist
                    self.btn_handler.click_update()

            # Mache ekliges Grau als Hintergrund
            self.screen.fill((20, 20, 20))

            # Blittet alle Sachen in der Liste self.to_draw in der Klasse
            # Draw_handler in der Datei handler.py
            self.draw.update()

            # Schlangen(Python) Zeugs
            pygame.display.update()
            self.clock.tick(60)

    def run(self):
        self.gameloop()


if __name__ == "__main__":
    # Application wird gestartet
    main = Main()
    main.run()

    # NICO IST EIN ** ** * ** * * *