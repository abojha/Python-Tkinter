from tkinter import *

root = Tk()
root.title("Using config to Update Widget")
root.geometry("400x400")

def something():
    my_label.config(text="This is new text", font=("Helvetica", 10))
    root.config(bg="blue")
    myButton.config(text="You have clicked",state=DISABLED)

global my_label
my_label = Label(root, text="This is my text", font=("Helvetica", 18))
my_label.pack(pady=10)

global mybutton
myButton = Button(root, text="Click Me", command=something)
myButton.pack()


root.mainloop()