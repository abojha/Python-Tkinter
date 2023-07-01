# Timers and Clocks
import tkinter as tk
import time


root = tk.Tk()
root.title('Clock')
root.geometry('600x400')


def clock():
    hour = time.strftime("%I")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    day = time.strftime("%A")
    am_pm = time.strftime("%p")
    timeZone = time.strftime("%Z")

    myLabel.config(text=f"{hour} : {minute} : {second} {am_pm}")
    myLabel.after(1000, clock)

    myLabel2.config(text=f"{timeZone} {day}")


# def update():
#     myLabel.config(text="New Text")


myLabel = tk.Label(root, text="", font=("Helvetica", 40), fg="green", bg="black")
myLabel.pack(pady=20)

myLabel2 = tk.Label(root, text="", font=("Helvetica", 14))
myLabel2.pack(pady=20)

clock()
# myLabel.after(5000, update)



root.mainloop()