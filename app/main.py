import tkinter as tk

root = tk.Tk()

root.title("Secret Santa Application")
root.geometry("1000x750")

label = tk.Label(root, text="Click to find out who is getting gifts for who in this years secret santa!")
label.pack(pady=10)

def on_randomize_click():
    label.config(text="Here are the pairings!")

randomizeButton = tk.Button(root, text="Generate List", command=on_randomize_click)
randomizeButton.pack(pady=10)

root.mainloop()