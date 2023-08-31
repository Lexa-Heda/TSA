# Autor:      Nico Freitag und Ludwig Schemmert
# Version:    v0
# Erstellt:   31.08.2023
# Bearbeitet: 31.08.2023

from decimal import Decimal, getcontext


class Main_class():
    def __init__(self):
        getcontext().prec = 16

        # Die Quadratzahl der Wurzel
        self.radicant = 2

        # Die wievielte Wurzel
        self.index = 2

        # Die Wurzel
        self.root_number = Decimal("3")

        # Intervallgröße
        self.size = Decimal("1")

        self.small_num = 0
        self.big_num = 0

        self.i = Dezimal("0")

    def start_funct(self):
        print("---------------------------------------------------------------------")
        print("Willkommen zu diesem kleinen Mathe Programm!")
        print("Es ist ganz einfach.")
        print("Wähle zwischen diesen Optionen, indem du die passende Zahl eingibst:")
        print("")
        print("1) Programm Test")
        print("2) WIP")
        print("3) WIP")
        print("")
        self.input = input("Wähle: ")

    def main_funct(self):
        if self.radicant == 0:
            self.found = True
            self.root_number = 0
        elif self.radicant < 0:
            self.radicant_neg = True
            self.found = True

        self.start_funct()

    def intervall(self):
        while True:
            if self.i * self.i < self.radicant:
                self.small_num = self.i
                self.i += self.size
            elif self.i * self.i > self.radicant:
                self.big_num = self.i
                self.size = self.size / 10
            elif self.i * self.i == self.radicant:
                self.found = True
                self.root_number = self.i

    def heron(self):
        pass

    def statistic(self):
        pass


if __name__ == "__main__":
    main = Main_class()
    main.main_funct()
