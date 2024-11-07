import tkinter as tk

class NameListPage(tk.Frame):
    def __init__(self, parent, name_list):
        super().__init__(parent, bg='lightpink')
        self.grid(row=0, column=0, stick="snew")
        self.name_list = name_list

        add_people_message = tk.Label(self, text="Type a name to add them to the Secret Santa List!", bg="lightpink")
        remove_people_message = tk.Label(self, text="Click the 'X' button to the right of a name to remove that person from the Secret Santa List!", bg="lightpink")

        add_people_message.pack(pady=20)
        remove_people_message.pack(pady=20)

        self.entry = tk.Entry(self)
        self.entry.pack(pady=5)

        add_button = tk.Button(self, text="Add", command=self.add_name)
        add_button.pack(pady=5)

        self.names_frame = tk.Frame(self, bg='lightpink')
        self.names_frame.pack(pady=10, padx=20, anchor="w")

        self.max_columns = 10

        self.display_names()

    def display_names(self):
        for widget in self.names_frame.winfo_children():
            widget.destroy()
        
        for i, name in enumerate(self.name_list.get_names()):
            row = i // self.max_columns
            col = i % self.max_columns

            name_label = tk.Label(self.names_frame, text=name, bg="lightpink", anchor="w")
            name_label.grid(row=row, column=col * 2, padx=5, pady=2, sticky="w")

            remove_button = tk.Button(self.names_frame, text="X", command=lambda n=name: self.remove_name(n))
            remove_button.grid(row=row, column=col * 2 + 1, padx=5, pady=2, sticky="w")

    def remove_name(self, name):
        res = self.name_list.remove_name(name)
        if res:
            self.display_names()

    def add_name(self):
        name = self.entry.get().strip()
        if name:
            self.name_list.add_name(name)
            self.entry.delete(0, tk.END)
            self.display_names()