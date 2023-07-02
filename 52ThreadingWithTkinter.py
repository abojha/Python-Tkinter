import tkinter as tk
import time
from random import randint
import threading

def fiveSeconds():
    time.sleep(5)
    label.config(text="5 Second is UP")

def randofunc():
    randomLabel.config(text=f"Random Number:: {randint(1, 100)}")
    



root = tk.Tk()
root.title('Threading With Tkinter')
root.geometry('500x400')

label = tk.Label(root, text="Hello Ji")
label.pack(pady=20)

button1 = tk.Button(root, text="5Secongs", command=threading.Thread(target=fiveSeconds).start())
button1.pack(pady=20)

button2 = tk.Button(root, text="Pick Random Number", command=randofunc)
button2.pack(pady=20)

randomLabel = tk.Label(root, text="")
randomLabel.pack(pady=20)


root.mainloop()