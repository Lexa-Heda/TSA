import sys
from sys import exit
import random



class Main_class():
    def __init__(self):
        self.square_number = 0
        self.number = 0
        self.eingabe = ""

        # 0 ist wenn du von einer Zahl die Quadratzahl sagen musst
        # 1 umgekehrt und 2 beides zuffällig immer mal
        self.mode = 0

        self.running = True

        self.learn_status = {}

        self.counter = 1

    def main_funct(self):
        self.start_funct()

        if self.mode == 0:
            self.sqaure_guess_funct()
        elif self.mode == 1:
            self.number_guess_funct()
        elif self.mode == 2:
            self.both_guess_funct()
        else:
            print("--------------------------------------")
            print("Please enter only number from 1 to 3.")
            print()
            self.main_funct()


    def start_funct(self):
        print("Welcome to this sqaure number learn program.")
        print("Do you want to guess square numbers from numbers or in the other way?")
        print()
        print("1) Square number guess")
        print("2) Number guess")
        print("3) Randomly both")
        print()
        self.eingabe = input("Choose: ")
        self.eingabe = int(self.eingabe) - 1

        self.to_number = input("Bis zu welcher Zahl wollen sie lernen?")

    def sqaure_guess_funct(self):
        while self.running:

            self.number = random.randint(1, 20)

            self.square_number = self.number^2

            print(f"Guess number {self.counter}")
            self.eingabe = input(f"Enter the square number from {self.number}: ")

            self.eingabe = int(self.eingabe)

            if self.eingabe == self.square_number:
                print("Right!")
            else:
                print("Wrong answer")
            print()
            self.counter += 1

    def number_guess_funct(self):
        while self.running:
            pass

    def both_guess_funct(self):
        while self.running:
            pass

if __name__ == "__main__":
    main_objekt = Main_class()
    main_objekt.main_funct()