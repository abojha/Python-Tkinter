from tkinter import *

root = Tk()

#Creating a Label Widget
myLabel1 = Label(root, text = "Hello World!").grid(row=0, column=0)
myLabel2 = Label(root, text = "Hello World!")
myLabel3 = Label(root, text = "Hello World!")
myLabel4 = Label(root, text = "Hello World!")
myLabel5 = Label(root, text = "Hello World!")
myLabel6 = Label(root, text = "Hello World!")

#Showing it onto the screen
# myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)
myLabel3.grid(row=1, column=1)

root.mainloop()