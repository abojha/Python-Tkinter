from tkinter import *
from PIL import ImageTk, Image

root = Tk()

#for title
root.title("Binary Dose")
#for icon
root.iconbitmap('favicon.ico')

#for exit button
# button_quit = Button(root, text="EXIT", command=root.quit)

#for Image
my_Img = ImageTk.PhotoImage(Image.open('logo.png'))
my_Label = Label(image=my_Img)
my_Label.pack()



root.mainloop()