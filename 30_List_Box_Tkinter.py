from tkinter import *

root = Tk()
root.title("List Box")
root.geometry("400x400")

# Create Frame and Scroll Bar
myFrame = Frame(root)
myScrollBar = Scrollbar(myFrame, orient=VERTICAL)

# List Box!
myListBox = Listbox(myFrame, width=50, yscrollcommand=myScrollBar.set, selectmode=MULTIPLE)

# Configure Scroll Bar
myScrollBar.config(command=myListBox.yview)
myScrollBar.pack(side=RIGHT, fill=Y)
myFrame.pack()
myListBox.pack(pady=15)





# Add Item to listBox
myListBox.insert(END, "This is an item")
myListBox.insert(END, "This is another item")

# Add list of items
myList = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]

for item in myList:
    myListBox.insert(END, item)

# Add item in specific position
myListBox.insert(2, "A new Item")


def functionDelete():
    myListBox.delete(ANCHOR)

def functionSelect():
    myLabel.config(text=myListBox.get(ANCHOR))

def functionDeleteAll():
    myListBox.delete(0, END)

def functionSelectAll():
    result = ''
    
    # print(myListBox.curselection())
    for item in myListBox.curselection():
        result = result + str(myListBox.get(item)) + "\n"

    myLabel.config(text=result)

def functionDeleteMultiple():
    for item in reversed(myListBox.curselection()):
        myListBox.delete(item)


myButton = Button(root, text="Delete", command=functionDelete)
myButton.pack(pady=10)


myButton2 = Button(root, text="Select", command=functionSelect)
myButton2.pack(pady=10)

myLabel = Label(root, text="")
myLabel.pack(pady=5)


myButton3 = Button(root, text="Delete All", command=functionDeleteAll)
myButton3.pack(pady=10)

myButton4 = Button(root, text="Select All", command=functionSelectAll)
myButton4.pack(pady=10)

myButton5 = Button(root, text="Delete Multiple", command=functionDeleteMultiple)
myButton5.pack(pady=10)

root.mainloop()