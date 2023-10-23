import os


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





if __name__ == "__main__":
    app = App()
    #app.run()
