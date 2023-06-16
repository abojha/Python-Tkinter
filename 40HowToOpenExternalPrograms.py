# How to Open EXternal Programs with Tkinter Python
from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("Open External Programs")
root.geometry("600x400")


def OpenProgram():
    myProgram = filedialog.askopenfilename()
    myLabel.config(text=myProgram)


myButton = Button(root, text="Open Program", command=OpenProgram)
myButton.pack(pady=20)

myLabel = Label(root, text="")
myLabel.pack(pady=20)

root.mainloop()
