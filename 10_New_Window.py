#New windows with tkinter and python
from tkinter import *

root = Tk()

def open():
    top = Toplevel()
    lbl = Label(top, text="Hello World").pack()
    btn2 = Button(top, text="Close Window", command=top.destroy).pack()

btn = Button(root, text="Open second window", command=open).pack()

mainloop()