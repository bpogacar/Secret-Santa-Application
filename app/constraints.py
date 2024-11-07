import tkinter as tk

class ConstraintsPage(tk.Frame):
    def __init__(self, parent, name_list):
        super().__init__(parent, bg='lightblue')
        self.grid(row=0, column=0, stick="snew")
        self.name_list = name_list

        add_people_message = tk.Label(self, text="Type a name in each box to add a constraint to the Secret Santa game. The person in the first box will be unable to give a present to the person in the second box.", bg="lightblue")
        remove_people_message = tk.Label(self, text="Click the 'X' button to the right of a constraint to remove it from the Secret Santa List!", bg="lightblue")

        add_people_message.pack(pady=20)
        remove_people_message.pack(pady=20)

        self.giver_entry = tk.Entry(self)
        self.giver_entry.pack(pady=5)

        self.receiver_entry = tk.Entry(self)
        self.receiver_entry.pack(pady=5)

        add_button = tk.Button(self, text="Add", command=self.add_constraint)
        add_button.pack(pady=5)

        self.constraints_frame = tk.Frame(self, bg='lightblue')
        self.constraints_frame.pack(pady=10, padx=20, anchor="w")

        self.max_columns = 5

        self.display_constraints()

    def display_constraints(self):
        for widget in self.constraints_frame.winfo_children():
            widget.destroy()

        i = 0
        
        for constraint in self.name_list.get_constraints():
            giver, receiver = constraint
            if giver == receiver:
                continue
            row = i // self.max_columns
            col = i % self.max_columns

            name_label = tk.Label(self.constraints_frame, text=f"{giver} ≠> {receiver}", bg="lightblue", anchor="w")
            name_label.grid(row=row, column=col * 2, padx=5, pady=2, sticky="w")

            remove_button = tk.Button(self.constraints_frame, text="X", command=lambda c=constraint: self.remove_constraint(c))
            remove_button.grid(row=row, column=col * 2 + 1, padx=5, pady=2, sticky="w")

            i += 1

    def remove_constraint(self, constraint):
        giver, receiver = constraint
        res = self.name_list.remove_constraint(giver, receiver)
        if res:
            self.display_constraints()

    def add_constraint(self):
        giver = self.giver_entry.get().strip()
        receiver = self.receiver_entry.get().strip()
        if giver and receiver:
            self.name_list.add_constraint(giver, receiver)
            self.giver_entry.delete(0, tk.END)
            self.receiver_entry.delete(0, tk.END)
            self.display_constraints()