import tkinter as tk
import pyttsx3




root = tk.Tk()
root.title('TextToSpeech')
root.geometry('800x500')



def talk():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(myEntry.get())
    engine.runAndWait()
    myEntry.delete(0, tk.END)


myEntry = tk.Entry(root, font=("Helvatica, 20"))
myEntry.pack(pady=20)

myButton = tk.Button(root, text="Speak", command=talk)
myButton.pack(pady=20)


root.mainloop()