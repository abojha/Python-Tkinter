from tkinter import *
from PIL import Image, ImageTk
from tkinter  import filedialog


root = Tk()


# root.filename = filedialog.askopenfilename(initialdir="F:\Python Tkinter\Images", title="Select a file", filetypes=(("png files", "*.png"), ("all files", "*.*")))
# my_label = Label(root, text=root.filename).pack()
# my_image = ImageTk.PhotoImage(Image.open(root.filename))
# my_imageLabel = Label(image=my_image).pack()

def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir="F:\Python Tkinter\Images", title="Select a file", filetypes=(("png files", "*.png"), ("all files", "*.*")))
    my_label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_imageLabel = Label(image=my_image).pack()


btn = Button(root, text="Opan a file", command=open).pack()

mainloop()