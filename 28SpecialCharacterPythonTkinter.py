from tkinter import *

root = Tk()
root.title("Special Characters")
root.geometry("400x400")

myLabl = Label(root, text='42'+ u'\u00a9', font=("Helvetica", 32)).pack(pady=10)

my_button = Button(root, text=u'\u00BB').pack(pady=10)



root.mainloop()