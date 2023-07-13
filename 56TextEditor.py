import tkinter as tk
from tkinter import filedialog
from tkinter import font
import os, sys
import win32
import win32print, win32api
from tkinter import colorchooser

root = tk.Tk()
root.title('Binary Dose - Text Editor')
root.geometry('1200x700')

# Set variable for open file name
global open_status_name
open_status_name = False

global selected
selected = False

# Create new_file function
def new_file():
    # Delete Previous Text
    my_text.delete("1.0", tk.END)

    # Update Status Bar
    root.title("New File - Text Editor")
    status_bar.config(text="New File     ")

    # set open file name to false
    global open_status_name
    open_status_name = False


def open_file():
    # Delete Previous Text
    my_text.delete(1.0, tk.END)

    # Grab File Name
    text_file = filedialog.askopenfilename(initialdir="F://Python-Tkinter/", title="Open File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("All Files", "*.*")))

    # Chekc if there is a file_name
    if text_file:
        # Get the file name which is currently open, in the global variable
        global open_status_name
        open_status_name = text_file

    # Update Statu Bar
    name = text_file
    status_bar.config(text=f"{name}     ")

    name = name.replace("F:/Python - Tkinter/", "")
    # Update title Bar
    root.title(f"{name} - Text Editor")
    
    # Open the file
    text_file = open(text_file, "r")
    # Read the data into stuff
    stuff = text_file.read()

    # Add Data to Text Box
    my_text.insert(tk.END, stuff)

    # Close the Open File
    text_file.close()


def save_as_file():
    text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir="F://Python-Tkinter/", title="Save As File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("All Files", "*.*")))

    if text_file:
        # Update Status Bar
        name = text_file
        status_bar.config(text=f"Saved :: {name}     ")
        name = name.replace("F:/Python - Tkinter/", "")
        root.title(f"{name} - Text Editor")

        # Save the file
        text_file = open(text_file, "w")
        text_file.write(my_text.get(1.0, tk.END))
        # Close the file
        text_file.close()

# Save File
def save_file():
    global open_status_name

    if open_status_name:
        # Save the file
        text_file = open(open_status_name, "w")
        text_file.write(my_text.get(1.0, tk.END))
        # Close the file
        text_file.close()

        status_bar.config(text=f"Saved :: {open_status_name}     ")
    else:
        save_as_file()

# function to print file
def print_file():
    # printer_name = win32print.GetDefaultPrinter()
    # status_bar.config(text=printer_name)

    # Grab the file name
    file_to_print = filedialog.askopenfilename(initialdir="F://Python-Tkinter/", title="Open File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("All Files", "*.*")))

    if file_to_print:
        win32api.ShellExecute(0, "print", file_to_print, None, ".", 0)

# function to select all text
def select_all(e):
    # Add sel tag to select all text
    my_text.tag_add("sel", '1.0', 'end')

# function to clear all text
def clear_all():
    my_text.delete(1.0, tk.END)

# function to cut text
def cut_text(e):
    global selected

    # Check to see if we use keyboard shortcuts
    if e:
        selected = root.clipboard_get()
    else:
        if my_text.selection_get():
            # Grab Selected text from text box
            selected = my_text.selection_get()
            # Delete Selected text from text box
            my_text.delete("sel.first", "sel.last")
            # Clear the clip board and append the selected text into it
            root.clipboard_clear()
            root.clipboard_append(selected)



def copy_text(e):
    global selected
    # Check to see if we use keyboard shortcuts
    if e:
        selected = root.clipboard_get()
    if my_text.selection_get():
        # Grab Selected text from text box
        selected = my_text.selection_get()
        # Clear the clip board and append the selected text into it
        root.clipboard_clear()
        root.clipboard_append(selected)

def paste_text(e):
    global selected 
    # Check to see if we use keyboard shortcuts
    if e:
        selected = root.clipboard_get()

    else:
        if selected:
            position = my_text.index(tk.INSERT)
            my_text.insert(position, selected)

def bold_text():
    # Create our font
    bold_font = font.Font(my_text, my_text.cget("font"))
    bold_font.configure(weight="bold")

    # Configure a tag
    my_text.tag_configure("bold", font=bold_font)

    # Defint current_tags
    current_tag = my_text.tag_names("sel.first")
    # If tag has been set bold
    if "bold" in current_tag:
        my_text.tag_remove("bold", "sel.first", "sel.last")
    else:
        my_text.tag_add("bold", "sel.first", "sel.last")

def italic_text():
    # Create our font
    italic_font = font.Font(my_text, my_text.cget("font"))
    italic_font.configure(slant="italic")

    # Configure a tag
    my_text.tag_configure("italic", font=italic_font)

    # Defint current_tags
    current_tag = my_text.tag_names("sel.first")
    # If tag has been set bold
    if "italic" in current_tag:
        my_text.tag_remove("italic", "sel.first", "sel.last")
    else:
        my_text.tag_add("italic", "sel.first", "sel.last")

def color_text():
    # Pick a Color
    my_color = colorchooser.askcolor()[1]

    if my_color:
        # Create our font
        color_font = font.Font(my_text, my_text.cget("font"))

        # Configure a tag
        my_text.tag_configure("colored", font=color_font, foreground=my_color)

        # Defint current_tags
        current_tag = my_text.tag_names("sel.first")
        # If tag has been set bold
        if "colored" in current_tag:
            my_text.tag_remove("colored", "sel.first", "sel.last")
        else:
            my_text.tag_add("colored", "sel.first", "sel.last")

# Change all text Color
def fg_color():
    my_color = colorchooser.askcolor()[1]
    my_text.config(fg=my_color)

# Change background Color
def bg_color():
    my_color = colorchooser.askcolor()[1]
    my_text.config(bg=my_color)


# Create a Tool Bar Frame
toolbar_frame = tk.Frame(root)
toolbar_frame.pack(fill=tk.X)

# Create Main Frame
my_frame = tk.Frame(root)
my_frame.pack(pady=5)

# Create a Vertical Scroll Bar for the Text Box
text_vertical_scroll = tk.Scrollbar(my_frame, orient='vertical')
text_vertical_scroll.pack(side=tk.RIGHT, fill=tk.Y)

# Create a Horizontal Scroll Bar for the Text Box
text_horizontal_scroll = tk.Scrollbar(my_frame, orient='horizontal')
text_horizontal_scroll.pack(side=tk.BOTTOM, fill=tk.X)

# Create Text Box
my_text = tk.Text(my_frame, width=97, height=25, font=("Helvetica", 16), selectbackground="yellow", selectforeground="black", undo=True, yscrollcommand=text_vertical_scroll.set, wrap="none",  xscrollcommand=text_horizontal_scroll.set)
my_text.pack()

# Configure our Scroll bar
text_vertical_scroll.config(command=my_text.yview)
text_horizontal_scroll.config(command=my_text.xview)

# Create a Menu
my_menu = tk.Menu(root)
root.config(menu=my_menu)

# Add File Menu
file_menu = tk.Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Print", command=print_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Add Edit Menu
edit_menu = tk.Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command= lambda: cut_text(False), accelerator="(Ctrl-x)")
edit_menu.add_command(label="Copy", command= lambda: copy_text(False), accelerator="(Ctrl-c)")
edit_menu.add_command(label="Paste", command= lambda: paste_text(False), accelerator="(Ctrl-v)")
edit_menu.add_separator()
edit_menu.add_command(label="Undo", command=my_text.edit_undo, accelerator="(Ctrl-z)")
edit_menu.add_command(label="Redo", command=my_text.edit_redo, accelerator="(Ctrl-y)")
edit_menu.add_separator()
edit_menu.add_command(label="Select All", command= lambda: select_all(True), accelerator="(Ctrl-a)")
edit_menu.add_command(label="Clear", command=clear_all, accelerator="(Ctrl-y)")


# Add Color Menu
color_menu = tk.Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Add Color", menu=color_menu)
color_menu.add_command(label="Change Selected Text", command=color_text)
color_menu.add_command(label="Change All Text", command=fg_color)
color_menu.add_command(label="Change Background Color", command=bg_color)
# Add Status Bar to Bottom
status_bar = tk.Label(root, text="Ready     ", anchor=tk.E)
status_bar.pack(fill=tk.X, side=tk.BOTTOM, ipady=5)

# Edit Bindings
root.bind('<Control-x>', cut_text)
root.bind('<Control-c>', copy_text)
root.bind('<Control-v>', paste_text)
# Select Bindings
root.bind('<Control-A>', select_all)
root.bind('<Control-a>', select_all)

# Create Buttons

# Bold Button
bold_button = tk.Button(toolbar_frame, text="Bold", command=bold_text)
bold_button.grid(row=0, column=0, sticky=tk.W, padx=5)

# Italic Button
italics_button = tk.Button(toolbar_frame, text="Italics", command=italic_text)
italics_button.grid(row=0, column=1, sticky=tk.W, padx=5)

# Undo Button
undo_button = tk.Button(toolbar_frame, text="Undo", command=my_text.edit_undo)
undo_button.grid(row=0, column=2, sticky=tk.W, padx=5)

# Redo Button
redo_button = tk.Button(toolbar_frame, text="Redo", command=my_text.edit_redo)
redo_button.grid(row=0, column=3, padx=5)

# Text Color
color_text_button = tk.Button(toolbar_frame, text="Text Color", command=color_text)
color_text_button.grid(row=0, column=4, padx=5)

root.mainloop()