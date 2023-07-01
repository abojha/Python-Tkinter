from tkinter import *

root = Tk()
root.title("Radio Buttons")
 

#Radio Buttons

# r = IntVar()
# r.set(2)

# def clicked(value):
#     label = Label(root, text=r.get()).pack()

# Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
# Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()
pizza = StringVar()
pizza.set("Tomato")

#Function to take action whenever clicked on radio buttons
def clicked(value):
    label = Label(root, text=value).pack()
MODES = [
    ("Tomato", "Tomato"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion"),
    ("Wheat", "Wheat"),
]

#Radio button implementation through loops
for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack()

#button
mybutton = Button(root, text="Click Me!", command=lambda: clicked(pizza.get()))
mybutton.pack()


mainloop()
