import tkinter as tk



root = tk.Tk()
root.title('Reset Spinbox')
root.geometry('500x350')

def reset():
    var = tk.IntVar(root)
    var.set(0)
    my_spin.config(textvariable=var)

var = tk.IntVar(root)
var.set(0)

my_spin = tk.Spinbox(root, from_=0, to=100, font=("Helvetica", 20), textvariable=var)
my_spin.pack(pady=20)

my_button = tk.Button(root, text="Reset spinner", command=reset)
my_button.pack(pady=20)

root.mainloop()