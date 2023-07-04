import tkinter as tk



root = tk.Tk()
root.title('Spin Box in Tkinter')
root.geometry('500x400')

def grab():
    spinValue = mySpin.get()
    myLabel.config(text=spinValue)

mySpin = tk.Spinbox(root, from_=0, to=10, font=("Helvetica", 20))
# mySpin = tk.Spinbox(root, values=("Abhay", "Anjali", "Mayank", "Chhavi"), font=("Helvetica", 20))
mySpin.pack(pady=20)

myButton = tk.Button(root, text="Submit", command=grab)
myButton.pack(pady=20)

myLabel = tk.Label(root, text="")
myLabel.pack(pady=20)

root.mainloop()