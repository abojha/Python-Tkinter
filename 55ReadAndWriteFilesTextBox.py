import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title('Read and Write into Files with Text Box')
root.geometry('500x450')

def openText():
    textFile = filedialog.askopenfilename(initialdir="F:\Python - Tkinter", title="Open Text file", filetypes=(("Text Files", "*.txt"),))
    textFile = open(textFile, "r")
    stuff = textFile.read()

    myText.insert(tk.END, stuff)
    textFile.close()

def saveText():
    textFile = filedialog.askopenfilename(initialdir="F:\Python - Tkinter", title="Open Text file", filetypes=(("Text Files", "*.txt"),))
    textFile = open(textFile, 'w')
    textFile.write(myText.get(1.0, tk.END))



myText = tk.Text(root, width=40, height=10, font=("Helvetica", 16))
myText.pack(pady=20)

openButton = tk.Button(root, text="Open Text Files", command=openText)
openButton.pack(pady=20)

saveButton = tk.Button(root, text="Save Files", command=saveText)
saveButton.pack(pady=20)
root.mainloop()