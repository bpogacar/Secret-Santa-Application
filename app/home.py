import tkinter as tk

class HomePage(tk.Frame):
    def __init__(self, parent, name_list):
        super().__init__(parent, bg='lightgreen')
        self.grid(row=0, column=0, stick="snew")
        self.name_list = name_list

        label = tk.Label(self, text="Click to find out who is getting gifts for who in this years Secret Santa!", bg="lightgreen")
        label.pack(pady=20)

        randomizeButton = tk.Button(self, text="Generate List", command=self.on_button_click)
        randomizeButton.pack(pady=20)

        self.result_frame = tk.Frame(self, bg="lightgreen")
        self.result_frame.pack(pady=20)

    def on_button_click(self):
        for widget in self.result_frame.winfo_children():
            widget.destroy()

        pairs = self.name_list.generate_pairs()

        if pairs:
            max_rows_per_column = 12
            curr_row = 0
            curr_column = 0

            for giver, receiver in pairs:
                pair_label = tk.Label(self.result_frame, text=f"{giver} -> ???", bg="lightgreen")
                pair_label.grid(row=curr_row, column=curr_column, padx=20, pady=5, sticky="w")

                pair_label.bind("<Enter>", lambda e, lbl=pair_label, r=receiver: self.show_receiver(lbl, r))
                pair_label.bind("<Leave>", lambda e, lbl=pair_label, g=giver: self.hide_receiver(lbl, g))

                curr_row += 1
                if curr_row > max_rows_per_column:
                    curr_row = 0
                    curr_column += 1
        else:
            error_label = tk.Label(self.result_frame, text="No valid pairings found. Please check your constraints and ensure there are names in the names list.", fg="red", bg="lightgreen")
            error_label.pack(pady=20)
    
    def show_receiver(self, label, receiver):
        label.config(text=f"{label.cget('text').split('->')[0].strip()} -> {receiver}")
    
    def hide_receiver(self, label, giver):
        label.config(text=f"{giver} -> ???")