import tkinter as tk



root = tk.Tk()
root.title('Hover On Popup')
root.geometry('500x400')

def buttonHover(e):
    myButton["bg"] = "white"
    statusLabel.config(text="I am Hovering Over the Button")

def buttonHoverLeave(e):
    myButton["bg"] = "SystemButtonFace"
    statusLabel.config(text="")

myButton = tk.Button(root, text="Click Me", font=("Helvetica",  28))
myButton.pack(pady=50)

statusLabel = tk.Label(root, text="", bd=1, relief=tk.SUNKEN, anchor=tk.E)
statusLabel.pack(fill=tk.X, side=tk.BOTTOM, ipady=2)


myButton.bind("<Enter>", buttonHover)
myButton.bind("<Leave>", buttonHoverLeave)

root.mainloop()