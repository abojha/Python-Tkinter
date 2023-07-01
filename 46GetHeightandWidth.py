import tkinter as tk



root = tk.Tk()
root.title('Get Height and Width')
root.geometry('800x800')

def info():
    dimensionsLabel = tk.Label(root, text=root.winfo_geometry())
    dimensionsLabel.pack(pady=20)

    heightLabel = tk.Label(root, text="height " + str(root.winfo_height()))
    heightLabel.pack(pady=20)

    widthLabel = tk.Label(root, text="width " + str(root.winfo_width()))
    widthLabel.pack(pady=20)

    xLabel = tk.Label(root, text="height " + str(root.winfo_x()))
    xLabel.pack(pady=20)

    yLabel = tk.Label(root, text="width " + str(root.winfo_y()))
    yLabel.pack(pady=20)

myButton = tk.Button(root, text="Click Me", command=info)
myButton.pack(pady=20)



root.mainloop()