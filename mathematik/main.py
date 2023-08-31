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
        self.root_number = Decimal("")
    def main_funct(self):
        self.input = input("Gebe eine Zahl ein: ")
        print(type(self.root_number))
        print(self.root_number)
        print()
        print(len(str(self.root_number)))


    def intervall(self):
        pass

    def heron(self):
        pass

if __name__ == "__main__":
    main = Main_class()
    main.main_funct()
