import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Tree View")
root.geometry("500x800")

# Add Style
style = ttk.Style()

# Pick a Theme
style.theme_use("default")

# Configure our treeview color
style.configure(
    "Treeview",
    background="#D3D3D3",
    foreground="black",
    rowheight=25,
    fieldbackground="D3D3D3",
)

# Change Selected Color
style.map("Treeview", background=[("selected", "blue")])


# Tree View Frame
tree_frame = tk.Frame(root)
tree_frame.pack(pady=20)

# Tree View Scrollbar
scroll = ttk.Scrollbar(tree_frame)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

# Create Tree View
my_tree = ttk.Treeview(tree_frame, yscrollcommand=scroll.set)
my_tree.pack(pady=20)

# Configure Scroll Bar
scroll.config(command=my_tree.yview)


# Define columns
my_tree["columns"] = ("Name", "ID", "Fav Pizza")

# Format Our Columns
my_tree.column("#0", width=0, stretch=tk.NO)
my_tree.column("Name", anchor=tk.W, width=140, minwidth=25)
my_tree.column("ID", anchor=tk.CENTER, width=100, minwidth=25)
my_tree.column("Fav Pizza", anchor=tk.W, width=140, minwidth=25)

# Create Headings
my_tree.heading("#0", text="", anchor=tk.W)
my_tree.heading("Name", text="Customer Name", anchor=tk.W)
my_tree.heading("ID", text="ID", anchor=tk.CENTER)
my_tree.heading("Fav Pizza", text="Favourite Pizza", anchor=tk.W)

# Add Data
data = [
    ["Abhay",  1, "Onion"],
    ["Anjali", 2, "Tomata"],
    ["Chhavi", 3, "Cheese"],
    ["Mintu",  4, "Bread"],
    ["Mintu",  5, "Bread"],
    ["Mintu",  6, "Bread"],
    ["Mintu",  7, "Bread"],
    ["Mintu",  8, "Bread"],
    ["Abhay",  9, "Onion"],
    ["Anjali", 10, "Tomata"],
    ["Chhavi", 11, "Cheese"],
    ["Abhay",  12, "Onion"],
    ["Anjali", 13, "Tomata"],
    ["Chhavi", 14, "Cheese"],
    ["Abhay",  15, "Onion"],
    ["Anjali", 16, "Tomata"],
    ["Chhavi", 17, "Cheese"],
    ["Abhay",  18, "Onion"],
    ["Anjali", 19, "Tomata"],
    ["Chhavi", 20, "Cheese"],
]

# Create Striped Row Tags
my_tree.tag_configure("oddrow", background="white")
my_tree.tag_configure("evenrow", background="blue")

global count
count = 0
for record in data:
    # if count % 2 == 0:
    my_tree.insert(
        parent="",
        index="end",
        iid=count,
        text="",
        values=(record[0], record[1], record[2]),
        tags=("evenrow" if count % 2 == 0 else "oddrow"),
    )
    # else:
    #     my_tree.insert(parent='', index='end', iid=count, text="",  values=(record[0], record[1], record[2]), tags=('oddrow'))
    count += 1

"""
my_tree.insert(parent='', index='end', iid=0, text="",  values=("Abhay", 1, "Onion"))
my_tree.insert(parent='', index='end', iid=1, text="",  values=("Anjali", 2, "Corn"))
my_tree.insert(parent='', index='end', iid=2, text="",  values=("Chhavi", 3, "Wheat"))
my_tree.insert(parent='', index='end', iid=3, text="",  values=("Mayank", 4, "Tomato"))
my_tree.insert(parent='', index='end', iid=4, text="",  values=("Shyam", 5, "Cheese"))

"""
# Add Child
# my_tree.insert(parent='', index='end', iid=5, text="Child",  values=("Lulu", 6, "Cheese"))
# my_tree.move('5', '0', '0')

addFrame = tk.Frame(root)
addFrame.pack(pady=20)


# Labels
nl = tk.Label(addFrame, text="Name")
nl.grid(row=0, column=0)
il = tk.Label(addFrame, text="ID")
il.grid(row=0, column=1)
tl = tk.Label(addFrame, text="Topping")
tl.grid(row=0, column=2)

# Entry boxes
name_box = tk.Entry(addFrame)
name_box.grid(row=1, column=0)
id_box = tk.Entry(addFrame)
id_box.grid(row=1, column=1)
topping_box = tk.Entry(addFrame)
topping_box.grid(row=1, column=2)


# Add Record Function
def add_record():
    global count
    my_tree.insert(
        parent="",
        index="end",
        iid=count,
        text=count,
        values=(name_box.get(), id_box.get(), topping_box.get()),
        tags=("evenrow" if count % 2 == 0 else "oddrow"),
    )

    # Clear the Boxes
    name_box.delete(0, tk.END)
    id_box.delete(0, tk.END)
    topping_box.delete(0, tk.END)
    # Increment the count
    count += 1


# Remove All Function
def remove_all():
    for record in my_tree.get_children():
        my_tree.delete(record)


# Remove One Function
def remove_one():
    x = my_tree.selection()[0]
    my_tree.delete(x)


# Remove Many Function
def remove_many():
    x = my_tree.selection()
    for record in x:
        my_tree.delete(record)

# Select Record
def select_record():
    # Clear Entry Boxes
    name_box.delete(0, tk.END)
    id_box.delete(0, tk.END)
    topping_box.delete(0, tk.END)

    # Grab Record Number
    selected =  my_tree.focus()

    # Grab Record Values
    values = my_tree.item(selected, 'values')

    name_box.insert(0, values[0])
    id_box.insert(0, values[1])
    topping_box.insert(0, values[2])


def save_record():
    # Grab Record Number
    selected =  my_tree.focus()

    # Save new Data
    my_tree.item(selected, text = "", values=(name_box.get(), id_box.get(), topping_box.get())) 

    # Clear Entry Boxes
    name_box.delete(0, tk.END)
    id_box.delete(0, tk.END)
    topping_box.delete(0, tk.END)

def move_up_record():
    rows = my_tree.selection()

    for row in rows:
        my_tree.move(row, my_tree.parent(row), my_tree.index(row)-1)

def move_down_record():
    rows = my_tree.selection()

    for row in reversed(rows):
        my_tree.move(row, my_tree.parent(row), my_tree.index(row)+1)

# Create Binding Clicker Function
def clicker(e):
    select_record()

# buttons
move_up_record_btn = tk.Button(root, text="Move Up", command=move_up_record)
move_up_record_btn.pack(pady=20)

move_down_record_btn = tk.Button(root, text="Move Down", command=move_down_record)
move_down_record_btn.pack(pady=20)

select_record_btn = tk.Button(root, text="Select Record", command=select_record)
select_record_btn.pack(pady=20)

save_record_btn = tk.Button(root, text="Save Record", command=save_record)
save_record_btn.pack(pady=20)

add_record_btn = tk.Button(root, text="Add Record", command=add_record)
add_record_btn.pack(pady=20)

remove_all_btn = tk.Button(root, text="Remove All", command=remove_all)
remove_all_btn.pack(pady=20)

remove_one_btn = tk.Button(root, text="Remove One", command=remove_one)
remove_one_btn.pack(pady=20)

remove_many_btn = tk.Button(root, text="Remove Many", command=remove_many)
remove_many_btn.pack(pady=20)


# Bindings
my_tree.bind("<Double-1>", clicker)
root.mainloop()
