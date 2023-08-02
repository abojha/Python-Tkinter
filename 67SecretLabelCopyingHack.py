import tkinter as tk



root = tk.Tk()
root.title('Secret Label Copying Hack')
root.geometry('500x350')

# Create a Label 1
my_label = tk.Label(root, text="Label 1", font=("Helvetica", 20))
my_label.pack(pady=20)

# Create String Var
# my_text = tk.StringVar()
# my_text.set("This is Label 2")

# Create Entry Box
my_entry = tk.Entry(root, 
                    font=("Helvetica", 20), 
                    bd=0
                    # ,state="readonly"
                    # ,textvariable=my_text
                    )
my_entry.insert(0, "This is cool Label 2")
my_entry.config(state="readonly")
my_entry.pack(pady=20)



root.mainloop()