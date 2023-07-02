import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title('Add Scroll Bar to Full Screen')
root.geometry('500x400')

# Create a Main Frame
mainFrame = tk.Frame(root)
mainFrame.pack(fill=tk.BOTH, expand=1)

# Create a Canvas
myCanvas = tk.Canvas(mainFrame)
myCanvas.pack(side=tk.LEFT, fill = tk.BOTH, expand=1)

# Add Scroll bar to Canvas
myScrollBar = ttk.Scrollbar(mainFrame, orient=tk.VERTICAL, command=myCanvas.yview)
myScrollBar.pack(side=tk.RIGHT, fill=tk.Y)


# Configure the Canvas
myCanvas.configure(yscrollcommand=myScrollBar.set)
myCanvas.bind('<Configure>', lambda e: myCanvas.configure(scrollregion=myCanvas.bbox("all")))

# Create another frame inside the canvas
secondFrame = tk.Frame(myCanvas)

# Add that new frame to a window inside the canvas
myCanvas.create_window((0, 0), window = secondFrame, anchor="nw")

for thing in range(100):
    tk.Button(secondFrame, text=f"Button : {thing}").grid(row=thing, column=0, pady=10)
    

root.mainloop()