import tkinter as tk
from tkinter import ttk
import random, time
from PIL import Image, ImageTk


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1280x720")
        self.root.title("Sternen-Casino")
        #self.icon = Image.open("filename")
        self.active = True

        self.titelbildschirm()
        self.gameloop()
    def create_GUI(self):
        pass

    def titelbildschirm(self):
        label = tk.Label(self.root, text="Press the button to start", font="Helvetica")
        label.pack(padx=10, pady=10)



        start_button = tk.Button(self.root, text="Start", command="exec(\"break\")")
        start_button.pack(pady=100)
        def toogle_label():
            current_state = label.cget("state")
            if current_state == "normal":
                label.config(state="disabled")
            else:
                label.config(state="normal")
            self.root.after(1000, toggle_label)
        while True:


            self.root.update()

    def gameloop(self):
        while self.active:
            self.update()

    def update(self):
        self.root.update()

if __name__ == "__main__":
    app = App()
    print("Du wirst diesen Print-Befehl niemals finden!")
