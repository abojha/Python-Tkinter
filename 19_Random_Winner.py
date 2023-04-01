from tkinter import *
from random import randint


root = Tk()
root.geometry("600x400")




def pick():
    listEntries = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Harry", "Ivy", "Jack", "Kate", "Leo", "Mary", "Nick", "Olivia", "Paul", "Quinn", "Rachel", "Sam", "Tina", "Uma", "Victor", "Wendy", "Xavier", "Yara", "Zack", "Anna", "Ben", "Claire", "Dan", "Emma", "Fred", "Gina", "Henry", "Isabel", "James", "Kelly", "Luke", "Mia", "Noah", "Oscar", "Penny", "Ryan", "Sara", "Tom", "Vera", "Will", "Zoe"]

    # convert list to set
    setEntries = set(listEntries)

    # convert set to list
    listUnique = list(setEntries)
    
    #Calculate the length of our unique_list -1
    ourNumber = len(listUnique) - 1

    # Select a random number between 0 to size of list - 1
    rando = randint(0, ourNumber)

    winLabel = Label(root, text=listUnique[rando], font=("Helvetica", 18))
    winLabel.pack(pady=20)

topLevel = Label(root, text="Win-O-Rama!", font=('Helvetica', 24))
topLevel.pack(pady=20)

winButton = Button(root, text="PICK OUR WINNER", font=('Helvetica', 24), command=pick)
winButton.pack(pady=20)

root.mainloop()