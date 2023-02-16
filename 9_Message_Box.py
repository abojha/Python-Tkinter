from tkinter import *
from tkinter import messagebox


root = Tk()

# Different types of message boxes in tkinter
# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
    response = messagebox.askokcancel("This is my Popup", "Hello World")
    Label(root, text=response).pack()

Button(root, text="popup", command=popup).pack()




mainloop()