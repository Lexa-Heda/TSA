import tkinter as tk
import time
import random

def start_app():
    # Diese Funktion wird aufgerufen, wenn der Startbutton gedrückt wird.
    root.destroy()  # Schließe den Startbildschirm
    # Hier kannst du deine eigentliche App-Logik einfügen

def toggle_label():
    # Diese Funktion wird verwendet, um den Schriftzug aufflackern zu lassen
    current_state = label.cget("state")
    if current_state == "normal":
        label.config(state="disabled")
    else:
        label.config(state="normal")
    root.after(2000, toggle_label)  # Alle 500 Millisekunden die Funktion erneut aufrufen

root = tk.Tk()
root.title("Start Screen")

label = tk.Label(root, text="Press any button to start", font=("Helvetica", 24))
label.pack(pady=20)

start_button = tk.Button(root, text="Start", command=start_app)
start_button.pack()

toggle_label()  # Starte das Aufflackern des Schriftzugs

root.mainloop()
