# Autor:      Nico Freitag und Ludwig Schemmert
# Version:    v0
# Erstellt:   31.08.2023
# Bearbeitet: 01.09.2023
from mpmath import mp
import time

class Timer:
    def __init__(self):
        self.start_zeit = None
        self.end_zeit = None
    def start_timer(self):
        self.start_zeit = time.time()
    def stop_timer(self):
        if self.start_zeit != None:
            self.end_zeit = time.time() - self.start_zeit
            self.start_zeit = None
            return self.end_zeit
        else:
            raise ValueError("Der timer wurde nicht gestartet")


class Main_class():
    def __init__(self):
        self.stellen = 16
        mp.dps = 16
        # Die Quadratzahl der Wurzel
        self.radicant = 2
        self.clock = Timer()
        # Die wievielte Wurzel
        self.index = 2

        # Die Wurzel
        self.root_number = 0

        # Intervallgröße
        self.size = 1
        self.small_num = 0
        self.big_num = 0

        self.i = 0

    def start_funct(self):
        print("Willkommen zu diesem kleinen Mathe Programm!")
        print("Es ist ganz einfach.")
        print("Wähle zwischen diesen Optionen, indem du die passende Zahl eingibst:")
        print("")
        print("1) Intervall Verfahren")
        print("2) Babylonisches Verfahren")
        print("3) WIP")
        print("")
        self.input = input("Wähle: ")
        self.i = 0


        if self.input == "1":
            #mach hier dein zeugs hin
            self.intervall()

        elif self.input == "2":
            self.radicant = int(input("Zahl zum Radizieren: "))
            try:
                self.stellen = int(input("Gebe die anzahl stellen ein die du haben möchtest: ")) + 1
                mp.dps = int(self.stellen)
            except:
                print("Gib eine Zahl ein!")
                self.main_funct()

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
        self.end_zeit = self.clock.stop_timer()
        print(
            f"Process ended Succesfully\nneeded Time: {self.end_zeit}\n\n--------------------------------------------------------------------------")
        self.main_funct()

    def found(self):
        if self.found():
            print()
            print("Programm wurde erfolgreich beendet.")
            print(f"Deine {self.index}. Wurzel von {self.radicant} ist {self.root_number}")


if __name__ == "__main__":
    main = Main_class()
    main.main_funct()
