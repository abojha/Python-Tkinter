from tkinter import *

root = Tk()
root.title("Create Multiple Entries")
root.geometry("700x500")

listEntries = []
def functionSomething():
    entryList = ""
    for entries in listEntries:
        entryList = entryList + str(entries.get()) + "\n"
        myLabel.config(text=entryList)

for y in range(5):
    for x in range(5):
        myEntry = Entry(root)
        myEntry.grid(row=y, column=x, pady=20, padx=5)
        listEntries.append(myEntry)


myButton = Button(root, text="Click Me!", command=functionSomething)
myButton.grid(row=5, column=0, pady=20)

myLabel = Label(root, text="")
myLabel.grid(row=6, column=0, pady=20)

root.mainloop()