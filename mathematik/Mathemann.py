# Autor:      Nico Freitag und Ludwig Schemmert
# Version:    v1
# Erstellt:   31.08.2023
# Bearbeitet: 31.08.2023

from decimal import Decimal, getcontext
from mpmath import mp
import time
import colorama
from colorama import Fore
from colorama import Style


class Main_class():
    def __init__(self):
        colorama.init()

        self.stellen = 64

        mp.dps = 64
        # Die Quadratzahl der Wurzel
        self.radicant = 2
        #self.clock = Timer()
        # Die wievielte Wurzel
        self.index = 2

        # Die Wurzel
        self.root_number = -42

        # Intervallgröße
        self.size = 1
        self.small_num = 0
        self.big_num = 0

        self.i = 0
        self.found = False

        self.root_number_stellen = 0

    def start_funct(self):
        print("--------------------------------------------------------------------------\n")
        print("Welcome to this math homework!")
        print("It´s simple.")
        print("Choose one of this options and enter the right number:")
        print()
        print("1) Interval nesting")
        print("2) Heron’s Method")
        print()
        self.input = input("Choose: ")

        try:
            self.radicant = float(input("Enter the number you want to root: "))
            #self.index = int(input("Enter the index: "))
            self.stellen = int(input("Geben Sie die Anzahl an Nachkommastellen ein die Sie berechnen wollen: "))
            mp.dps = int(self.stellen) + 1
        except:
            print(f"{Fore.RED}Geben Sie eine Zahl ein!{Style.RESET_ALL}")
            self.main_funct()

        if self.radicant < 0:
            print(f"{Fore.RED}Aus negativen Zahlen kann man {Fore.YELLOW}KEINE{Fore.RED} Wurzeln ziehen!{Style.RESET_ALL}")
            self.main_funct()
            return None
        elif self.radicant == 0:
            self.root_number = 0
            self.statistic()
            self.main_funct()

        if self.input == "1":
            for i in range(self.stellen):
                if self.found:
                    self.statistic()
                else:
                    #if self.root_number_stellen <= self.stellen:
                    self.intervall()

            self.root_number = self.i
            self.statistic()

        elif self.input == "2":
            #self.clock.start_timer()
            self.A = mp.mpf(self.radicant)
            self.s_a = mp.mpf(8)
            self.s_b = mp.mpf(1)
            for i in range(self.stellen):
                if i == 0:
                    self.babylon(True)
                else:
                    self.babylon()
            self.root_number = self.s_a
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
            elif self.i * self.i > self.radicant:
                self.big_num = self.i
                self.size = self.size / 10
                self.i = self.small_num
                break
            elif self.i * self.i == self.radicant:
                self.found = True
                self.root_number = self.i
                break

    def babylon(self, s=False):
        self.s_a = mp.mpf((self.s_a + self.s_b) / 2)
        self.s_b = mp.mpf(self.A / self.s_a)

    def statistic(self):
        #self.end_zeit = self.clock.stop_timer()
        self.end_zeit = "unendlich"
        print()
        if self.root_number > 0:
            print(f"{Fore.GREEN}Your root number is {Fore.LIGHTGREEN_EX}{self.root_number}{Fore.GREEN}.{Style.RESET_ALL}")
            print(f"{Fore.GREEN}Your root number is -{Fore.LIGHTGREEN_EX}{self.root_number}{Fore.GREEN}.{Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}Your root number is {Fore.LIGHTGREEN_EX}{self.root_number}{Fore.GREEN}.{Style.RESET_ALL}")
        print(f"Process ended succesfully\nNeeded Time: {self.end_zeit} sek\n\n")
        self.main_funct()

if __name__ == "__main__":
    main = Main_class()
    main.main_funct()
