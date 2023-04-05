from tkinter import *
from random import randint


root = Tk()
root.geometry("600x400")
root.title("Delete Labels")

def functionDelete():
    # myLabel.pack_forget()
    myLabel.destroy()
    myButton['state'] = NORMAL


def functionClick():
    global myLabel
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    e.delete(0, 'end')
    myLabel.pack(pady=10)
    myButton['state'] = DISABLED




e = Entry(root, width=50, font=("Helvetica", 30))
e.pack(padx=10, pady=10)

myButton = Button(root, text="Enter Your Name", command=functionClick)
myButton.pack(pady=10)

buttonDelete = Button(root, text="Delete Text", command=functionDelete)
buttonDelete.pack(pady=10)

root.mainloop()