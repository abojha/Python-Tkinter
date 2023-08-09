import tkinter as tk
from tkinter import messagebox
import random


root = tk.Tk()
root.title('Tile Matching Game')
root.geometry('460x450')

# Create our Matches
global matches
matches = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
# Shuffle our matches
random.shuffle(matches)

# Create Our Frame
my_frame = tk.Frame(root)
my_frame.pack(pady=10)

# Define Some Variables
global winner
winner = 0
Count = 0
answer_list = []
answer_dict = {}

# functions
def reset():
    global matches, winner
    winner=0
    # Create our Matches
    matches = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
    # Shuffle our matches
    random.shuffle(matches)

    # Reset Label
    my_label.config(text="")

    # Reset Tiles
    button_list = [b0, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11]
    for button in button_list:
        button.config(bg="SystemButtonFace", state="normal", text="")


def win():
    my_label.config(text="Congratulation! You Win")
    button_list = [b0, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11]
    for button in button_list:
        button["bg"] = "blue"
    

def button_click(b, number):
    global Count, answer_list, answer_dict, Counting_moves, winner

    if b["text"] == "" and Count < 2:
        b["text"] = matches[number]
        # Add Number to answer list
        answer_list.append(number)
        # Add Number to answer dict
        answer_dict[b] = matches[number]
        # Increment Our Counter
        Count += 1

    # Start to determine correct or not
    if len(answer_list) == 2:
        if matches[answer_list[0]] == matches[answer_list[1]]:
            my_label.config(text = "MATCH")

            for key in answer_dict:
                key["state"] = "disable"
                key["bg"] = "yellow"
            Count = 0
            answer_dict = {}
            answer_list = []
            winner += 1
            if winner == 6:
                win()
        else:
            # my_label.config(text="DOH!")
            Count = 0
            answer_list = []
            # Message box
            messagebox.showinfo("Incorrect", "Incorrect")

            # Reset the Button
            for key in answer_dict:
                key["text"] = ""
            answer_dict = {}




# Define our Button
b0 = tk.Button(my_frame, text="", font=("Helvetica", 20), height=3, width=6, command=lambda:button_click(b0, 0), relief="groove")
b1 = tk.Button(my_frame, text="", font=("Helvetica", 20), height=3, width=6, command=lambda:button_click(b1, 1), relief="groove")
b2 = tk.Button(my_frame, text="", font=("Helvetica", 20), height=3, width=6, command=lambda:button_click(b2, 2), relief="groove")
b3 = tk.Button(my_frame, text="", font=("Helvetica", 20), height=3, width=6, command=lambda:button_click(b3, 3), relief="groove")
b4 = tk.Button(my_frame, text="", font=("Helvetica", 20), height=3, width=6, command=lambda:button_click(b4, 4), relief="groove")
b5 = tk.Button(my_frame, text="", font=("Helvetica", 20), height=3, width=6, command=lambda:button_click(b5, 5), relief="groove")
b6 = tk.Button(my_frame, text="", font=("Helvetica", 20), height=3, width=6, command=lambda:button_click(b6, 6), relief="groove")
b7 = tk.Button(my_frame, text="", font=("Helvetica", 20), height=3, width=6, command=lambda:button_click(b7, 7), relief="groove")
b8 = tk.Button(my_frame, text="", font=("Helvetica", 20), height=3, width=6, command=lambda:button_click(b8, 8), relief="groove")
b9 = tk.Button(my_frame, text="", font=("Helvetica", 20), height=3, width=6, command=lambda:button_click(b9, 9), relief="groove")
b10 = tk.Button(my_frame, text="", font=("Helvetica", 20), height=3, width=6, command=lambda:button_click(b10, 10), relief="groove")
b11 = tk.Button(my_frame, text="", font=("Helvetica", 20), height=3, width=6, command=lambda:button_click(b11, 11), relief="groove")

# Grib our Button
b0.grid(row=0, column=0)
b1.grid(row=0, column=1)
b2.grid(row=0, column=2)
b3.grid(row=0, column=3)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)
b7.grid(row=1, column=3)

b8.grid(row=2, column=0)
b9.grid(row=2, column=1)
b10.grid(row=2, column=2)
b11.grid(row=2, column=3)

my_label = tk.Label(root, text="")
my_label.pack(pady=10)


# Create a Menu
menu = tk.Menu(root)
root.config(menu=menu)

# Create an Options Dropdown menu
option_menu = tk.Menu(menu, tearoff=False)
menu.add_cascade(label="Options", menu=option_menu)
option_menu.add_command(label="Reset Game", command = reset)
option_menu.add_separator()
option_menu.add_command(label="Exit", command = quit)

root.mainloop()