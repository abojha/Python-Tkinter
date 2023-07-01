from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("400x400")
root.title("Image Button")

def thing():
    myLabel.config(text = "You clicked the button")

loginButton = PhotoImage(file='loginButton.png')



imgLabel = Label(image = loginButton)
# imgLabel.pack(pady=20)

myButton = Button(root, image = loginButton, command=thing, borderwidth=0)
myButton.pack(pady=20)

myLabel = Label(root, text='')
myLabel.pack(pady = 20)








root.mainloop()