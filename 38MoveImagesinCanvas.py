import tkinter as tk



root = tk.Tk()
root.title('Move Images In Canvas')
root.geometry('800x600')

w = 600
h = 400
x = w/2
y = h/2
 
myCanvas = tk.Canvas(root, width=w, height=h, bg="white")
myCanvas.pack(pady=20)


# Add Images to Canvas
img = tk.PhotoImage(file="Numbers/1.png")
myImage = myCanvas.create_image(0, 0, anchor=tk.NW, image=img)

def left(event):
    x = -10
    y = 0
    myCanvas.move(myImage, x, y)

def right(event):
    x = 10
    y = 0
    myCanvas.move(myImage, x, y)

def up(event):
    x = 0
    y = -10
    myCanvas.move(myImage, x, y)

def down(event):
    x = 0
    y = 10
    myCanvas.move(myImage, x, y)

def pressing(event):
    x = 0
    y = 0
    if event.char == "a": x=-10
    if event.char == "d": x=10
    if event.char == "w": y=-10
    if event.char == "x": y=10
    myCanvas.move(myImage, x, y)

root.bind("<Key>", pressing)

root.bind("<Left>", left)
root.bind("<Right>", right)
root.bind("<Up>", up)
root.bind("<Down>", down)

root.mainloop()
