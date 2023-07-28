import tkinter as tk



root = tk.Tk()
root.title('Delete or Disable Menu Items')
root.geometry('500x500')

def new_file():
    pass

def open_file():
    pass

def delete_menu():
    file_menu.delete("New")

def disable_menu():
    file_menu.entryconfig("New", state="disable")

def enable_menu():
    file_menu.entryconfig("New", state="normal")

# Create Menu
my_menu = tk.Menu(root)
root.config(menu=my_menu)

# Add Menu Items
file_menu = tk.Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)

# Add dropdown Items
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)

# buttons
delete_menu = tk.Button(root, text="Delete Menu", command=delete_menu)
delete_menu.pack(pady=20)

disable_menu = tk.Button(root, text="Disable New", command=disable_menu)
disable_menu.pack(pady=20)

enable_menu = tk.Button(root, text="Enable New", command=enable_menu)
enable_menu.pack(pady=20)

root.mainloop()