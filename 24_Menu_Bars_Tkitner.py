from tkinter import *

root = Tk()
root.title("Menu Bars")
root.geometry("400x400")

def our_command():
    pass

myMenu = Menu(root)
root.config(menu=myMenu)

# Create a Menu Item
menuFile = Menu(myMenu)
myMenu.add_cascade(label="File", menu=menuFile)
menuFile.add_command(label="New", command=our_command)
menuFile.add_separator()
menuFile.add_command(label="Exit", command=root.quit)

# Crate a edit menu
menuEdit = Menu(myMenu)
myMenu.add_cascade(label="Edit", menu=menuEdit)
menuEdit.add_command(label="Cut", command=our_command)
menuEdit.add_separator()
menuEdit.add_command(label="Copy", command=our_command)

root.mainloop()