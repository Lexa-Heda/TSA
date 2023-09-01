# Autor:      Nico Freitag und Ludwig Schemmert
# Version:    v1
# Erstellt:   31.08.2023
# Bearbeitet: 31.08.2023

from decimal import Decimal, getcontext
from mpmath import mp
import time


class Main_class():
    def __init__(self):
        self.stellen = 64

        mp.dps = 64
        # Die Quadratzahl der Wurzel
        self.radicant = 2
        #self.clock = Timer()
        # Die wievielte Wurzel
        self.index = 2

        # Die Wurzel
        self.root_number = 0

        # Intervallgröße
        self.size = 1
        self.small_num = 0
        self.big_num = 0

        self.i = 0
        self.found = False

        self.root_number_stellen = 0

    def start_funct(self):
        print("Willkommen zu diesem kleinen Mathe Programm!")
        print("Es ist ganz einfach.")
        print("Wähle zwischen diesen Optionen, indem du die passende Zahl eingibst:")
        print("")
        print("1) Intervall Verfahren")
        print("2) Babylonisches Verfahren")
        print("")
        self.input = input("Wähle: ")
        self.i = 0

        try:
            self.radicant = int(input("Gib die Zahl ein, die du radizieren möchtest: "))
            self.stellen = int(input("Gib die anzahl Nachkommastellen ein die du berechnen möchtest: "))
            mp.dps = int(self.stellen) + 1
        except:
            print("Gib eine Zahl ein!")
            self.main_funct()

        if self.input == "1":
            for i in range(self.stellen):
                if self.found:
                    self.statistic()
                else:
                    if self.root_number_stellen <= self.stellen:
                        self.intervall()

            self.root_number = self.i
            self.statistic()

        elif self.input == "2":
            self.clock.start_timer()
            self.A = mp.mpf(self.radicant)
            self.s_a = mp.mpf(8)
            self.s_b = mp.mpf(1)
            for i in range(self.stellen):
                if i == 0:
                    self.babylon(True)
                else:
                    self.babylon()
            print(str(self.s_a))
            self.statistic()

    def main_funct(self):
        if self.radicant < 0:
            self.root_number = None
            self.found = True

        self.start_funct()

    def intervall(self):
        while True:
            if self.i * self.i < self.radicant:
                self.small_num = self.i
                self.i += self.size
                #print("Kleiner")
                #print(f"I = {self.i}")
                #print(f"Small num = {self.small_num}")
            elif self.i * self.i > self.radicant:
                self.big_num = self.i
                self.size = self.size / 10
                self.i = self.small_num
                self.root_number_stellen += 1
                #print("Größer")
                break
            elif self.i * self.i == self.radicant:
                self.found = True
                self.root_number = self.i
                #print("Gleich")
                break

    def babylon(self, s=False):
        self.s_a = mp.mpf((self.s_a + self.s_b) / 2)
        self.s_b = mp.mpf(self.A / self.s_a)

    def statistic(self):
        #self.end_zeit = self.clock.stop_timer()
        self.end_zeit = "unendlich"
        print()
        print()
        print(f"Your root number is {self.root_number}")
        print(f"Process ended succesfully\nNeeded Time: {self.end_zeit} sek\n\n--------------------------------------------------------------------------")
        self.main_funct()

if __name__ == "__main__":
    main = Main_class()
    main.main_funct()
