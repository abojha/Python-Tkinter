# How to resize image in tkinter python
import tkinter as tk
from PIL import ImageTk, Image



root = tk.Tk()
root.title('Resize Image')
root.geometry('800x500')

# Open Image
myPic = Image.open("Images/1.png")

# Resize Image
resized = myPic.resize((225, 100), Image.ANTIALIAS)

# Store the resized image into newPic
newPic = ImageTk.PhotoImage(resized)

myLabel = tk.Label(root, image=newPic)
myLabel.pack(pady=20)


root.mainloop()