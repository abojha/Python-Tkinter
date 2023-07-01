import tkinter as tk
from random import choice, shuffle



root = tk.Tk()
root.title('Word Jumble Game')
root.geometry('600x400')



def shuffler():

    # Clear answer Entry
    answerEntry.delete(0, tk.END)

    # Clear answer Label
    answerLabel.config(text="")

    # Clear Hint Label
    hintLabel.config(text="")

    # Reset Hint Count
    global hintCount
    hintCount = 0

    # List of Countries
    listCountries = ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua", "Barbuda", "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan"]
    
    # Pick random country from listCountries
    global word
    word = choice(listCountries)
    word = word.lower()

    # Break apart our chosen word
    breakApartList = list(word)
    shuffle(breakApartList)

    # Turn shuffled List into a word
    global shuffledWord
    shuffledWord = "".join(breakApartList)

    myLabel.config(text=shuffledWord)

def answer():
    if answerEntry.get().lower() == word:
        answerLabel.config(text="Correct")
    
    else:
        answerLabel.config(text=f"Incorrect! Answer was {word}")

# Create Hint Counter
global hintCount
hintCount = 0
# Create Hint Function
def hint(count):
    global hintCount
    hintCount = count

    # Get the length of choosen word
    wordLength = len(word)

    # Show Hit
    if count < wordLength:
        hintLabel.config(text=word[:hintCount+1])
        hintCount+=1



myLabel = tk.Label(root, text="", font=('Helvetica', 48))
myLabel.pack(pady=20)

answerEntry = tk.Entry(root, font=("Helvetica", 24))
answerEntry.pack(pady=20)

buttonFrame = tk.Frame()
buttonFrame.pack(pady=20)



answerButton = tk.Button(buttonFrame, text="Answer", command=answer)
answerButton.grid(row=0, column=0, padx=10)

shuffleButton = tk.Button(buttonFrame, text="Shuffle", command=shuffler)
shuffleButton.grid(row=0, column=1, padx=10)

hintButton = tk.Button(buttonFrame, text="Hint", command=lambda: hint(hintCount))
hintButton.grid(row=0, column=2, padx=10)

answerLabel = tk.Label(root, text="", font=("Helvetica", 18))
answerLabel.pack(pady=20)

hintLabel = tk.Label(root, text="", font=("Helvetica", 14))
hintLabel.pack(pady=10)

shuffler()
root.mainloop()