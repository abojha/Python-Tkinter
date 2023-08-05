import tkinter as tk



root = tk.Tk()
root.title('One Sided Padding')
root.geometry('500x550')
root.config(bg="blue")

# my_label = tk.Label(root, text="My Text", font=("Helvetica", 20), bg="white", fg="black")
# my_label.pack(pady=(50, 0))

# my_label2 = tk.Label(root, text="My Text 2", font=("Helvetica", 20), bg="white", fg="black")
# my_label2.pack()


my_label = tk.Label(root, text="My Text", font=("Helvetica", 20), bg="white", fg="black")
my_label.grid(row=0, column=0, pady=50, padx=(50, 0))

my_label2 = tk.Label(root, text="My Text 2", font=("Helvetica", 20), bg="white", fg="black")
my_label2.grid(row=0, column=1)




root.mainloop()