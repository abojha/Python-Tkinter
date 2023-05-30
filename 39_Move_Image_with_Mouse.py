import tkinter as tk



root = tk.Tk()
root.title('Move Iamges with Mouse')
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

def moves(e):
    #e.x
    #e.y
    global img
    img = tk.PhotoImage(file="Numbers/1.png")
    myImage = myCanvas.create_image(e.x, e.y, image=img)
    myLabel.config(text = f"x = {str(e.x)} and y = {str(e.y)}")



myLabel = tk.Label(root, text="")
myLabel.pack(pady=20)


myCanvas.bind('<B1-Motion>', moves)

root.mainloop()