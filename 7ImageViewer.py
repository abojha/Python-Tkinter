from email.mime import image
from faulthandler import disable
from tkinter import *
from turtle import backward
from PIL import Image, ImageTk

root = Tk()


#All Images
img1 = ImageTk.PhotoImage(Image.open('Images/1.png'))
img2 = ImageTk.PhotoImage(Image.open('Images/2.png'))
img3 = ImageTk.PhotoImage(Image.open('Images/3.png'))
img4 = ImageTk.PhotoImage(Image.open('Images/4.png'))
img5 = ImageTk.PhotoImage(Image.open('Images/5.png'))

#Image List
Images_List = [img1, img2, img3, img4, img5]


#Adding a status bar
status = Label(root, text="Image 1 of " + str(len(Images_List)), bd=1, relief=SUNKEN, anchor=E)

myLabel = Label(image=Images_List
[0])
myLabel.grid(row=0, column=0, columnspan=3)

def forward(image_number):
    global myLabel
    global button_for
    global button_back
    myLabel.grid_forget()

    myLabel = Label(image= Images_List[image_number-1])

    button_for = Button(root, text=">>", command=lambda: forward(image_number+1))

    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    status = Label(root, text="Image " + str(image_number) +  " of " + str(len(Images_List)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

    if image_number == 5:
        button_for = Button(root, text=">>", state=DISABLED)

    myLabel.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_for.grid(row=1, column=2)

def back(image_number):
    global myLabel
    global button_for
    global button_back

    myLabel.grid_forget()

    myLabel = Label(image= Images_List[image_number-1])

    button_for = Button(root, text=">>", command=lambda: forward(image_number+1))

    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    #Update Status Bar
    status = Label(root, text="Image " + str(image_number) +  " of " + str(len(Images_List)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)
    

    myLabel.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_for.grid(row=1, column=2)



button_back = Button(root, text="<<", command=back, state=DISABLED)
button_Exit = Button(root, text="Exit", command=root.quit)
button_for = Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_Exit.grid(row=1, column=1)
button_for.grid(row=1, column=2)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)
root.mainloop()