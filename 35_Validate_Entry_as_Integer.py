from tkinter import *

root = Tk()
root.title("Entry widget as an Integer")
root.geometry("400x400")

def Number():
    try:
        int(myBox.get())
        answer.config( text = "That is a Number")
    
    except ValueError:
        answer.config( text="Thats is not a Number")



myLabel = Label(root, text="Enter a Number")
myLabel.pack(pady=20)

myBox = Entry(root)
myBox.pack(pady=10)

myButton = Button(root, text="Enter a Number", command=Number)
myButton.pack(pady=5)


answer = Label(root, text="")
answer.pack(pady=20)

root.mainloop()