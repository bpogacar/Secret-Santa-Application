import tkinter as tk

class NameListPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg='lightpink')
        self.grid(row=0, column=0, stick="snew")

        add_people_message = tk.Label(self, text="Type a name people to add someone to the Secret Santa List!")
        remove_people_message = tk.Label(self, text="*** to remove people from the Secret Santa List!")

        add_people_message.pack(pady=50)