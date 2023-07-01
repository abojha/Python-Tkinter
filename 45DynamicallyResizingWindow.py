# Dynamically Resizing Windows
import tkinter as tk



root = tk.Tk()
root.title('Dynamically Resizing Windows')
root.geometry('800x800')

def resize():
    h = heightEntry.get()
    w = widthEntry.get()
    root.geometry(f"{w}x{h}")
    # root.geometry("{width}x{height}".format(width=w, height=h))


widthLabel = tk.Label(root, text="Width:")
widthLabel.pack(pady=20)
widthEntry = tk.Entry(root)
widthEntry.pack()

heightLabel = tk.Label(root, text="Height:")
heightLabel.pack(pady=20)
heightEntry = tk.Entry(root)
heightEntry.pack()

myButton = tk.Button(root, text="Rezie", command=resize)
myButton.pack(pady=20)



root.mainloop()