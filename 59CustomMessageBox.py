import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.title('Custom Message Box')
root.geometry('300x300')

def choice(option):
    pop.destroy()
    if option == "yes":
        my_label.config(text="You clicked Yes")
    else:
        my_label.config(text="You clicket No")

def clicker():
    global pop
    pop = tk.Toplevel(root)
    pop.title("My Popup")
    pop.geometry("250x150")
    pop.config(bg="green")

    global me
    me = tk.PhotoImage(file="Images/stop50.png")

    pop_label = tk.Label(pop, text="Would You Like to Proceed", bg="green", fg="white", font=("Helvetica", 10))
    pop_label.pack(pady=10)

    my_frame = tk.Frame(pop, bg="green")
    my_frame.pack(pady=5)

    my_pic = tk.Label(my_frame, image=me, borderwidth=0)
    my_pic.grid(row=0, column=0, padx=10)

    yes = tk.Button(my_frame, text="Yes", command=lambda:choice("yes"), bg="orange")
    yes.grid(row=0, column=1)

    no = tk.Button(my_frame, text="No", command=lambda:choice("np"), bg="red")
    no.grid(row=0, column=2)



my_button = tk.Button(root, text="Click me!", command=clicker)
my_button.pack(pady=50)

my_label = tk.Label(root, text="")
my_label.pack(pady=20)

root.mainloop()