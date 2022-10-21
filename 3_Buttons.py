from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Look! I clikced a Button!")
    myLabel.pack()


myButton = Button(root, text="Click Me!", pady=50, command=myClick, fg="blue", bg="black")
myButton.pack()


root.mainloop()