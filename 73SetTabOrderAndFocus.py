import tkinter as tk



root = tk.Tk()
root.title('Set Tab Order and Focus')
root.geometry('500x550')

# Create Some Entry Boxes
red_entry = tk.Entry(root, bg="red", font=("Helvetica", 20))
red_entry.pack(pady=20)
white_entry = tk.Entry(root, bg="white", font=("Helvetica", 20))
white_entry.pack(pady=20)
blue_entry = tk.Entry(root, bg="blue", font=("Helvetica", 20))
blue_entry.pack(pady=20)

# Pick Focus
red_entry.focus()

# Change Tab Order
def TabOrder():
    blue_entry.focus()
    widgets = [blue_entry, white_entry, red_entry]
    for w in widgets:
        w.lift()


# my_button = tk.Button(root, text="Change Tab Order")
# my_button.pack(pady=20)
TabOrder()
root.mainloop()