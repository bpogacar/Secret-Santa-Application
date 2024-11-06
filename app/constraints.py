import tkinter as tk
from main import container

class ConstraintsPage():
    def __init__(self):
        super().__init__(container, bg='lightblue')
        self.grid(row=0, column=0, stick="snew")