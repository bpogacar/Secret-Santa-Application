import tkinter as tk
from main import container

class HomePage(tk.Frame):
    def __init__(self):
        super().__init__(container, bg='lightgreen')
        self.grid(row=0, column=0, stick="snew")

        label = tk.Label(self, text="Click to find out who is getting gifts for who in this years secret santa!", bg="lightgreen")
        label.pack(pady=50)

        def on_randomize_click():
            label.config(text="Here are the pairings!")

        randomizeButton = tk.Button(self, text="Generate List", command=on_randomize_click)
        randomizeButton.pack(pady=50)

