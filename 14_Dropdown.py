from tkinter import *


root = Tk()

def show():
    myLabel = Label(root, text=clicked.get()).pack()

option = [
    "Monday", "Tuesday", "Wednesday", "Thursday"
]
clicked = StringVar()
clicked.set(option[0])
drop = OptionMenu(root, clicked, *option)
drop.pack()

mybtn = Button(root, text="Click", command=show).pack()
mainloop() 