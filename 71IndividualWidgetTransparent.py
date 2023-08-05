import tkinter as tk



root = tk.Tk()
root.title('Individual Widget Transparent')
root.geometry('500x550')

root.wm_attributes('-transparentcolor', root['bg'])

my_frame = tk.Frame(root, width=200, height=200)
my_frame.pack(pady=20, ipadx=10, ipady=10)

my_label = tk.Label(my_frame, text="My Text", font=("Helvetica", 20), fg="white")
my_label.pack(pady=20)

root.mainloop()