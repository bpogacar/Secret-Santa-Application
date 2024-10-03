import tkinter as tk

class NameListPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg='lightpink')
        self.grid(row=0, column=0, stick="snew")