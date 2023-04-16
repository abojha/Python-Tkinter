from tkinter import *

root = Tk()
root.title("Menu Bars")
root.geometry("400x400")

def our_command():
    pass

myMenu = Menu(root)
root.config(menu=myMenu)

def functionFileNew():
    functionHideAllFrames()
    newFileFrame.pack(fill="both", expand=1)
    label = Label(newFileFrame, text="You clicked a New file").pack()

    # to see what the winfo_children return
    child_label = Label(newFileFrame, text=newFileFrame.winfo_children())
    child_label.pack(pady=10)


def functionEditCut():
    functionHideAllFrames()
    cutEditFrame.pack(fill="both", expand=1)

    
# Hide all frame function
def functionHideAllFrames():
    # Loop through all the children and delete them
    for widget in newFileFrame.winfo_children():
        widget.destroy()
    # Loop through all the children and delete them
    for widget in cutEditFrame.winfo_children():
        widget.destroy()

    newFileFrame.pack_forget()
    cutEditFrame.pack_forget()

# Create a Menu Item
menuFile = Menu(myMenu)
myMenu.add_cascade(label="File", menu=menuFile)
menuFile.add_command(label="New", command=functionFileNew)
menuFile.add_separator()
menuFile.add_command(label="Exit", command=root.quit)

# Crate a edit menu
menuEdit = Menu(myMenu)
myMenu.add_cascade(label="Edit", menu=menuEdit)
menuEdit.add_command(label="Cut", command=functionEditCut)
menuEdit.add_separator()
menuEdit.add_command(label="Copy", command=our_command)

# Create a Option Menu 
menuOption = Menu(myMenu)
myMenu.add_cascade(label="Options", menu=menuOption)
menuOption.add_command(label="Find", command=our_command)
menuOption.add_command(label="Find Next", command=our_command)


# Create some frames
newFileFrame = Frame(root, width=400, height=400, bg="red")
cutEditFrame = Frame(root, width=400, height=400, bg="blue")
root.mainloop()