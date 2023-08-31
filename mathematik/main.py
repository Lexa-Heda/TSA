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

        # Intervallgröße
        self.i

        # Die Wurzel
        self.root_number = Decimal("3")

        self.small_num = 0
        self.big_num = 0

    def start_funct(self):
        print("---------------------------------------------------------------------")
        print("Willkommen zu diesem kleinen Mathe Programm!")
        print("Es ist ganz einfach.")
        print("Wähle zwischen diesen Optionen, indem du die passende Zahl eingibst:")
        print("\n")
        print("1) Programm Test")
        print("2) WIP")
        print("3) WIP")
        print("\n")
        print("\n")
        self.input = input("")

    def main_funct(self):
        self.start_funct()

    def intervall(self):
        if radicant <= 0:
            self.found = True

        #for i in range(self.radicant):
        #    if i * i < radicant:
        #        self.small_num = i
        #    elif i * i > self.radicant:
        #        self.big_num = i
        #    elif i * i == self.radicant:
        #        self.found = True

    def heron(self):
        pass

    def statistic(self):
        pass


if __name__ == "__main__":
    main = Main_class()
    main.main_funct()
