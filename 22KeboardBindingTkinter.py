from tkinter import *

root =  Tk()
root.title("Keyboard Binding in Python Tkinter")
root.geometry("400x400")
def clicker(event):
    myLabel = Label(root, text="You clicked a Button: " + event.keysym)
    myLabel.pack()

myButton = Button(root, text="Click Me")
myButton.pack(pady=20)

"""
Events used here:
Button-1, Button-3, Enter, Leave, FocusIn, FocusOut, Return, Key
"""
myButton.bind("<Key>", clicker)

root.mainloop()