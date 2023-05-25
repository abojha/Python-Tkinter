from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Use Tabs in Tkinter")
root.geometry("400x400")

# Define a tab (Notebook)
myNotebook = ttk.Notebook(root)
myNotebook.pack()

def functionHide():
    myNotebook.hide(1)

def functionShow():
    myNotebook.add(myFrame2, text="Red Tab")

def functionNavigate():
    myNotebook.select(1)

myFrame1 = Frame(myNotebook, width=500, height=400, bg="blue")
myFrame2 = Frame(myNotebook, width=500, height=400, bg="red")
myFrame3 = Frame(myNotebook, width=500, height=400, bg="green")

myFrame1.pack(fill="both", expand=1)
myFrame2.pack(fill="both", expand=1)
myFrame3.pack(fill="both", expand=1)

myNotebook.add(myFrame1, text="Blue Tab")
myNotebook.add(myFrame2, text="Red Tab")
myNotebook.add(myFrame3, text="Green Tab")

# Hide a Tab
myButton = Button(myFrame1, text="Hide Tab 2", command=functionHide).pack(pady=10)

# Show a Tab
myButton2 = Button(myFrame1, text="Show Tab 2", command=functionShow).pack(pady=10)

# Navigate a Tab
myButton3 = Button(myFrame1, text="Navigate to Tab2", command=functionNavigate).pack(pady=10)
root.mainloop()