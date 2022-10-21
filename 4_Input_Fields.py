from tkinter import *

root = Tk()

#For input field "Entery" widget is used
e = Entry(root, width=50, bg="blue", fg="white")
e.pack()

#insert is used to place some text already inside the input field
e.insert(0, "Enter Your Name")

#function
def myClick():
    myLabel = Label(root, text="Hello " + e.get())
    myLabel.pack()

#Button
Btn = Button(root, text="Click Me", command=myClick)
Btn.pack()

# #this function get whatever you type in input field
# e.get()

root.mainloop()