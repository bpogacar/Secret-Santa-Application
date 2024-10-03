import tkinter as tk
from home import HomePage
from namepage import NameListPage
from contraints import ConstraintsPage

root = tk.Tk()

root.title("Secret Santa Application")
root.geometry("1000x750")


def change_frame(frame):
    frame.tkraise()

menu_bar = tk.Menu(root)

pages_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Pages", menu=pages_menu)

container = tk.Frame(root)
container.pack(fill="both", expand=True)
container.grid_columnconfigure(0, weight=1)
container.grid_rowconfigure(0, weight=1)

homepage = HomePage(container)
namelist_page = NameListPage(container)
contraints_page = ConstraintsPage(container)

pages_menu.add_command(label="Home Page", command=lambda: change_frame(homepage))
pages_menu.add_command(label="Edit Namelist", command=lambda: change_frame(namelist_page))
pages_menu.add_command(label="Add constraints", command=lambda: change_frame(contraints_page))
pages_menu.add_command(label="Exit", command=root.quit)

root.config(menu=menu_bar)

change_frame(homepage)

root.mainloop()