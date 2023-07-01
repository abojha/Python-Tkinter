from tkinter import *


root = Tk()

def show():
    myLabel = Label(root, text=var.get()).pack()

var = StringVar()
c = Checkbutton(root, text="Check this Box, I dare you", variable=var, onvalue="Pizza", offvalue="Chole Batoore")
c.deselect()
c.pack()

myLabel = Label(root, text=var.get()).pack()

mybtn = Button(root, text="Show Selection", command=show).pack()

mainloop()