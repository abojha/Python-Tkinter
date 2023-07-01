from tkinter import *
from PIL import  ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.geometry("400x200")


def graph():
    housePrices = np.random.normal(2500000, 25000, 5000)
    plt.hist(housePrices, 50)
    plt.show()

my_button = Button(root, text="Click Me", command=graph)
my_button.pack()

root.mainloop()