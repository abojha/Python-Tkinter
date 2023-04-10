from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Dropdown and Combobox")
root.geometry("400x400")

# function
def functionSelected(event):
    myLabel = Label(root, text=clicked.get()).pack(pady=20)

def functionCombo(event):
    myLabel = Label(root, text=combo.get()).pack(pady=20)
# list of days
listOption = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# A variable name clicked
clicked = StringVar()
clicked.set(listOption[0])

# Drop Down Menu
drop = OptionMenu(root, clicked, *listOption, command=functionSelected)
drop.pack(pady=20)

# myButton = Button(root, text="Select from List", command=functionSelected)
# myButton.pack(pady=20)

# Combo Box
combo = ttk.Combobox(root, values=listOption)
combo.current(0)
combo.bind("<<ComboboxSelected>>", functionCombo)
combo.pack()

root.mainloop()