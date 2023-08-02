import tkinter as tk



root = tk.Tk()
root.title('Position Label the Right Way')
root.geometry('500x700')

label1 = tk.Label(root,
                  text="Stuff\nStuff Stuff\nStuff Stuff Stuff"
                  ,font=("Helvetica", 18)
                  ,bd=1, relief=tk.SUNKEN)
label1.pack(pady=20, ipadx=10, ipady=10)

label2 = tk.Label(root,
                  text="Stuff\nStuff Stuff\nStuff Stuff Stuff"
                  ,font=("Helvetica", 18)
                  ,bd=1, relief=tk.SUNKEN
                  ,justify="right")
label2.pack(pady=20, ipadx=10, ipady=10)

label3 = tk.Label(root,
                  text="Stuff\nStuff Stuff\nStuff Stuff Stuff"
                  ,font=("Helvetica", 18)
                  ,bd=1, relief=tk.SUNKEN
                  , justify="left")
label3.pack(pady=20, ipadx=10, ipady=10)


root.mainloop()