import os
import random


class App:
    def __init__(self):
        self.active = True

        self.vocabeln = ["hallo", "Ich wohne in..."]
        self.vocabeln_franz = ["Bonjour", "J'habite a..."]

        self.themen_fragen = [
            [], # Mathe
            [], # Geschichte
            [] # Chemie
        ]
    def run(self):
        while self.active:
            print("____________________________________________________\n"
                  "Das ist ein Lernprogramm!"
                  "")

    def menu(self):
        print("Menu:"
              "--------------------------------------"
              ""
              "Suche dir eine Option aus:"
              ""
              "1) Französisch Vokabeln Abfragen"
              "2) Neue Vokabeln hinzufügen"
              "3) Mathethesen abfragen"
              "4) Geschichte abfragen")
        self.choice = int(input("Auswahl"))


        

    def ask_voc(self):
        self.index = random.randint(0, len(self.vocabeln) + 1)
        self.voc_ger = self.vocabeln[self.index]
        self.voc_frz = self.vocabeln_franz[self.index + 1]

        print(f"Was ist die Übersetzung von: {self.voc_ger}?")
        check = input("Press Enter to show the Lösung:")
        print(f"Die Übersetzung lautet: {self.voc_frz}!")




if __name__ == "__main__":
    app = App()
    #app.run()
