from tkinter import *


root = Tk()
root.title("Tkinter with Classes")

class anji:

    def __init__(self, master):
        self.myFrame = Frame(master)
        self.myFrame.pack()

        self.myButton = Button(master, text="Click Me!")
        self.myButton.pack(pady=20)
    
    def clicker():
        print("Look at You....... You clicked a button!")


e = anji(root)

root.mainloop()