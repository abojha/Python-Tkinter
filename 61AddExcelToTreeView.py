import tkinter as tk
import pandas as pd
from tkinter import ttk, filedialog



root = tk.Tk()
root.title('Add Excel to Tree View')    
root.geometry('700x500')

# Create Fram
my_frame = tk.Frame(root)
my_frame.pack(pady=20)

# Create Treeview
my_tree = ttk.Treeview()

# file_open function
def file_open():
    file_name = filedialog.askopenfilename(
        initialdir="F:/Python - Tkinter/",
        title="Open a File",
        filetypes=(("xlsx files", "*.xlsx"), ("All files", "*.*")))
    
    if file_name:
        try:
            file_name = r"{}".format(file_name)
            df = pd.read_excel(file_name)
        except ValueError:
            my_label.config(text="File Couldn't Open Try Again!!")
        except FileNotFoundError:
            my_label.config(text="File Not Found")
    
    # Clear Old Tree view
    clear_tree()

    # Setup New Tree View
    my_tree["column"] = list(df.columns)
    my_tree["show"] = "headings"

    # Loop Through Column List for headers
    for column in my_tree["column"]:
        my_tree.heading(column, text=column)

    # Put data in Tree View
    df_rows = df.to_numpy().tolist()
    for row in df_rows:
        my_tree.insert("", "end", values=row)
    
    # Pack the TreeView
    my_tree.pack()

def clear_tree():
    my_tree.delete(*my_tree.get_children())



# Add a Menu
my_menu = tk.Menu(root)
root.config(menu=my_menu)


# Add Menu Dropdown
file_menu = tk.Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Spreadsheets", menu=file_menu)
file_menu.add_command(label="Open", command=file_open)

my_label = tk.Label(root, text="")
my_label.pack(pady=20)
root.mainloop()