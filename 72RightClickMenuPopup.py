import tkinter as tk



root = tk.Tk()
root.title('Right Click Menu Popup')
root.geometry('500x550')

my_label = tk.Label(root, text="", font=("Helvetica", 20))
my_label.pack(pady=20)


def Hello():
    my_label.config(text="Hello")

def Goodbye():
    my_label.config(text="GoodBye")

def my_popup(e):
    my_menu.tk_popup(e.x_root, e.y_root)
# My Menu
my_menu = tk.Menu(root, tearoff=False)
my_menu.add_command(label="Say Hello", command=Hello)
my_menu.add_command(label="Say GoodBye", command=Goodbye)
my_menu.add_separator()
my_menu.add_command(label="Exit", command=root.quit)


root.bind('<Button-3>', my_popup)
root.mainloop()