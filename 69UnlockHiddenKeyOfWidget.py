import tkinter as tk



root = tk.Tk()
root.title('Unlock All the Keys of Widgets')   
root.geometry('500x550')

my_label = tk.Label(root, text="My label", font=("Helvetica", 18))
my_label.pack(pady=20)

# List all the attribute of a widget
# my_label.keys()

# for key in my_label.keys():
#     print(key)

# Access the content of each attribute
print(my_label['text'])


root.mainloop()