import tkinter as tk
from namer import nameit


root = tk.Tk()
root.title('Use Other Python Programs')
root.geometry('500x350')

def greet():
    name = my_box.get()
    my_label.config(text=nameit(name))
# greet = nameit("Abhay")
my_box = tk.Entry(root)
my_box.pack(pady=20)

my_label = tk.Label(root, text="", font=("Helvetica", 20))
my_label.pack(pady=20)

my_button = tk.Button(root, text="Click Me!", command=greet)
my_button.pack(pady=20)
root.mainloop()