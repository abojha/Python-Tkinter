from tkinter import *
from random import randint


root = Tk()
root.geometry("400x400")
root.title("Delete Labels")

myLabel = Label(root)

# def functionDelete():
#     myLabel.grid_forget()
#     # myLabel.destroy()
#     myButton['state'] = NORMAL


# Pack system
# def functionClick():
#     global myLabel
#     hello = "Hello " + e.get()
#     myLabel = Label(root, text=hello)
#     e.delete(0, 'end')
#     myLabel.pack(pady=10)
#     myButton['state'] = DISABLED

# Grid System
def functionClick():
    global myLabel
    myLabel.destroy()
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    e.delete(0, 'end')
    myLabel.grid(row = 3, column = 0, pady=10)
    # myButton['state'] = DISABLED




e = Entry(root, width=17, font=("Helvetica", 30))
e.grid(row = 0, column = 0, padx=10, pady=10)

myButton = Button(root, text="Enter Your Name", command=functionClick)
myButton.grid(row = 1, column = 0, pady=10)

# buttonDelete = Button(root, text="Delete Text", command=functionDelete)
# buttonDelete.grid(row = 2, column = 0, pady=10)

root.mainloop()