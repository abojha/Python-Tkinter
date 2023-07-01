import tkinter as tk
import pygame


root = tk.Tk()
root.title('Sounds and Music')
root.geometry('500x500')

pygame.mixer.init()

def play():
    pygame.mixer.music.load("Sounds/audio1.mp3")
    pygame.mixer.music.play(loops=0)


def stop():
    pygame.mixer.music.stop()

myButton = tk.Button(root, text="Play", font=("Helvetica, 32"), command=play)
myButton.pack(pady=20)

stopButton = tk.Button(root, text="Stop", command=stop)
stopButton.pack(pady=20)

root.mainloop()