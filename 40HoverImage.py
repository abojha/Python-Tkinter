# Hover Image Animation
import tkinter as tk
# from PIL import ImageTk, Image


root = tk.Tk()
root.title('Hover Mouse On Image')
root.geometry('800x500')

def change(e):
    myPic = tk.PhotoImage(file="Images/2.png")
    myLabel.config(image=myPic)
    myLabel.image = myPic

def changeBack(e):
    myPic = tk.PhotoImage(file="Images/1.png")
    myLabel.config(image=myPic)
    myLabel.image = myPic


myPic = tk.PhotoImage(file="Images/1.png")
myLabel = tk.Label(root, image=myPic)
myLabel.pack(pady=20)


myLabel.bind("<Enter>", change)
myLabel.bind("<Leave>", changeBack)





root.mainloop()