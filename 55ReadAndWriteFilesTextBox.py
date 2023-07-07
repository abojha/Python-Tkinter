import tkinter as tk
from tkinter import filedialog
from tkinter import font

root = tk.Tk()
root.title('Read and Write into Files with Text Box')
root.geometry('500x600')

def openText():
    textFile = filedialog.askopenfilename(initialdir="F:\Python - Tkinter", title="Open Text file", filetypes=(("Text Files", "*.txt"),))
    title = textFile
    textFile = open(textFile, "r")
    stuff = textFile.read()

    myText.insert(tk.END, stuff)
    textFile.close()

    root.title(f'{title} - Touch Pad')

def saveText():
    textFile = filedialog.askopenfilename(initialdir="F:\Python - Tkinter", title="Open Text file", filetypes=(("Text Files", "*.txt"),))
    textFile = open(textFile, 'w')
    textFile.write(myText.get(1.0, tk.END))

def addImage():
    # Add Image
    global myImage
    myImage = tk.PhotoImage(file="Images/1.png")
    position = myText.index(tk.INSERT)
    myText.image_create(position, image=myImage)

def select():
    selected = myText.selection_get()
    myLabel.config(text=selected)

def bolder():
    boldFont = font.Font(myText, myText.cget("font"))
    boldFont.configure(weight="bold")

    myText.tag_configure("bold", font=boldFont)

    currentTag = myText.tag_names("sel.first")

    if "bold" in currentTag:
        myText.tag_remove("bold", "sel.first", "sel.last")
    else:
        myText.tag_add("bold", "sel.first", "sel.last")

def italic():
    italicFont = font.Font(myText, myText.cget("font"))
    italicFont.configure(slant="italic")

    myText.tag_configure("italic", font=italicFont)

    currentTag = myText.tag_names("sel.first")

    if "italic" in currentTag:
        myText.tag_remove("italic", "sel.first", "sel.last")
    else:
        myText.tag_add("italic", "sel.first", "sel.last")

myFrame = tk.Frame(root)
myFrame.pack(pady=10)
# Create Scroll Bar
textScroll = tk.Scrollbar(myFrame)
textScroll.pack(side=tk.RIGHT, fill=tk.Y)

myText = tk.Text(myFrame, width=40, height=10, font=("Helvetica", 16), selectbackground="yellow", selectforeground="black", yscrollcommand=textScroll, undo=True)

# Configure Scroll bar
textScroll.config(command=myText.yview)
myText.pack()



openButton = tk.Button(root, text="Open Text Files", command=openText)
openButton.pack(pady=20)

saveButton = tk.Button(root, text="Save Files", command=saveText)
saveButton.pack(pady=20)

ImageButton = tk.Button(root, text="Add Image", command=addImage)
ImageButton.pack(pady=5)

selectButton = tk.Button(root, text="Select", command=select)
selectButton.pack(pady=5)

boldButton = tk.Button(root, text="bold", command=bolder)
boldButton.pack(pady=5)

italicButton = tk.Button(root, text="italic", command=italic)
italicButton.pack(pady=5)

redoButton = tk.Button(root, text="Redo", command=myText.edit_redo)
redoButton.pack(pady=5)

undoButton = tk.Button(root, text="undo", command=myText.edit_undo)
undoButton.pack(pady=5)

myLabel = tk.Label(root, text="")
myLabel.pack(pady=5)


root.mainloop()