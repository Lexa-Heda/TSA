import sys
from sys import exit
import random
import colorama
from colorama import Fore, Style


class Main_class():
    def __init__(self):
        self.to_guess_number = 0
        self.square_number = 0
        self.number = 0
        self.eingabe = ""

        # 0 ist wenn du von einer Zahl die Quadratzahl sagen musst
        # 1 umgekehrt und 2 beides zuffällig immer mal
        self.mode = 0

        self.running = True

        self.learn_status = {}

        self.counter = 1

        self.found_number = True

        self.last_number = 0

        self.number_history = []

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
            print("Please enter only numbers from 1 to 3.")
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

        self.to_number = input("Up to which number do you want to learn? ")
        self.exclude_numbers = input("Enter the number up to which you don´t want to learn: ")

        self.to_number = int(self.to_number)
        self.exclude_numbers = int(self.exclude_numbers) + 1

        print()

    def sqaure_guess_funct(self):
        while self.running:

            #while self.last_number == self.number:
            #    self.number = random.randint(self.exclude_numbers, self.to_number)

            while True:
                for i in range(2):
                    self.number_in_list = i in self.number_history
                    if not self.number_in_list:
                        continue
                    if self.number == self.number_history[i]:
                        self.number = random.randint(self.exclude_numbers, self.to_number)


            self.to_guess_number = self.number * self.number

            print(f"{Fore.LIGHTWHITE_EX}---------------------------------------------------------{Style.RESET_ALL}")
            print(f"{Fore.LIGHTBLACK_EX}Guess number {self.counter}{Style.RESET_ALL}")
            self.eingabe = input(f"{Fore.YELLOW}Enter the square number from {Fore.LIGHTYELLOW_EX}{self.number}{Fore.YELLOW}:{Style.RESET_ALL} ")

            self.eingabe = int(self.eingabe)

            if self.eingabe == self.to_guess_number:
                #self.value = self.learn_status.__contains__(key)

                #if value:
                #self.learn_status[self.number] += 1
                #else:
                #    self.learn_status[self.number] = 0

                print(f"{Fore.GREEN}Right answer!{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}Wrong answer.{Fore.GREEN}{Style.RESET_ALL}")
                print(f"{Fore.RED}The right answer was {Fore.LIGHTRED_EX}{self.to_guess_number}{Fore.RED}.{Style.RESET_ALL}")

                #self.value = self.learn_status.__contains__(key)

                #if value:
                #self.learn_status[self.number] -= 1
                #else:
                #    self.learn_status[self.number] = 0

            print(self.learn_status)
            print()
            self.counter += 1

            #self.last_number = self.number
            self.number_history.append(self.number)

    def number_guess_funct(self):
        while self.running:
            pass

    def both_guess_funct(self):
        while self.running:
            pass

if __name__ == "__main__":
    main_objekt = Main_class()
    main_objekt.main_funct()