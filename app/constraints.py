import tkinter as tk

class ConstraintsPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg='lightblue')
        self.grid(row=0, column=0, stick="snew")