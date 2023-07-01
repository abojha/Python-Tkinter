# Progress Bar in Tkinter Python
import tkinter as tk
from tkinter import ttk
import time



root = tk.Tk()
root.title('Progress Bar')
root.geometry('600x400')

def step():
    myProgress['value'] += 10
    myLabel.config(text=myProgress['value'])
    # myProgress.start(10)

    # for x in range(5):
    #     myLabel.config(text=myProgress['value'])
    #     myProgress['value'] += 20
    #     root.update_idletasks()
    #     time.sleep(1)

def stop():
    myProgress.stop()

myProgress = ttk.Progressbar(root, orient='horizontal', length=300, mode='determinate' )
myProgress.pack(pady=20)


myButton = tk.Button(root, text="Progress", command=step)
myButton.pack(pady=20)

myButton2 = tk.Button(root, text="Stop", command=stop)
myButton2.pack(pady=20)

myLabel = tk.Label(root, text="")
myLabel.pack(pady=20)


root.mainloop()