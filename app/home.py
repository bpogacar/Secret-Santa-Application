import tkinter as tk

class HomePage(tk.Frame):
    def __init__(self, parent, name_list):
        super().__init__(parent, bg='lightgreen')
        self.grid(row=0, column=0, stick="snew")

        label = tk.Label(self, text="Click to find out who is getting gifts for who in this years secret santa!", bg="lightgreen")
        label.pack(pady=50)

        randomizeButton = tk.Button(self, text="Generate List", command='''INSERT METHOD HERE''')
        randomizeButton.pack(pady=50)

