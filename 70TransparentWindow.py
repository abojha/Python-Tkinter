import tkinter as tk
import tkinter.ttk as ttk



root = tk.Tk()
root.title('Transparent Window')
root.geometry('500x550')

# Transparency
root.attributes('-alpha',  0.3)

# Create slide function
def slide(x):
    root.attributes('-alpha', my_slider.get())
my_label = tk.Label(root, text="Hello World", font=("Helvetica", 20))
my_label.pack(pady=20)

# Slider
my_slider = ttk.Scale(root, from_=0.1, to=1.0, value=0.7, orient='horizontal', command=slide)
my_slider.pack(pady=20)

# function for making the window solid
def make_solid(e):
    new.attributes('-alpha',  1)

# function for creating a new window
def new_window():
    global new
    new = tk.Toplevel()
    new.attributes('-alpha',  0.3)
    new.bind('<Button-1>', make_solid)

# New Window
new_window = tk.Button(root, text="New Window", command=new_window)
new_window.pack(pady=20)

root.mainloop()