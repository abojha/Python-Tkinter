from tkinter import *
from PIL import ImageTk, Image
from random import randint
import random

root = Tk()
root.title("FlashCards")
root.geometry("600x600")

# Create Flash Card Random
def functionRandomMath():
    # Crate Two Random Numbers
    global num1, num2
    num1 = randint(0, 10)
    num2 = randint(0, 10)

    # Create Images
    global addImage1
    global addImage2

    addImage1 = ImageTk.PhotoImage(Image.open('Numbers/' + str(num1) + ".png"))
    addImage2 = ImageTk.PhotoImage(Image.open('Numbers/' + str(num2) + ".png"))

    # Put Flashcards Images On the Screen
    add1.config(image=addImage1)
    add2.config(image=addImage2)


# Function to verify the Addition Answer
def functionAddAnswer():
    answer = num1 + num2
    # print(entryAddAnswer.get())
    if int(entryAddAnswer.get()) == answer:
        response = "Correct " + str(num1) + " + " + str(num2) + " = " + str(answer)
    else:
        response = "Wrong " + str(num1) + " + " + str(num2) + " = " + str(answer) + " NOT " + entryAddAnswer.get()
    
    answerMessage.config(text=response)
    entryAddAnswer.delete(0, 'end')

    functionRandomMath()

# Function for Addition
def functionAddition():
    hideAllFrames()
    frameAddition.pack(fill="both", expand=1)

    labelAdd = Label(frameAddition, text="ADDITION FLASHCARD", font=("Helvetica", 18), bg="white").pack(pady=15)

    # Crate a frame for number pic
    frameNumberPic = Frame(frameAddition, width=400, height=300, bg="white")
    frameNumberPic.pack()

    # Crate Two Random Numbers
    global num1, num2
    num1 = randint(0, 10)
    num2 = randint(0, 10)

    #Create Three Labels in frameNumberPic
    global add1, add2
    add1 = Label(frameNumberPic)
    add2 = Label(frameNumberPic)
    mathSign = Label(frameNumberPic, text="+", font=("Helvetica", 28), bg="white")

    # Grid Our Labels
    add1.grid(row=0, column=0)
    mathSign.grid(row=0, column=1)
    add2.grid(row=0, column=2)

    # Create Images
    global addImage1
    global addImage2

    addImage1 = ImageTk.PhotoImage(Image.open('Numbers/' + str(num1) + ".png"))
    addImage2 = ImageTk.PhotoImage(Image.open('Numbers/' + str(num2) + ".png"))

    # Put Flashcards Images On the Screen
    add1.config(image=addImage1)
    add2.config(image=addImage2)

    # Create Answer Entry Box and Button
    global entryAddAnswer
    entryAddAnswer = Entry(frameAddition, font=("Helvetica", 18))
    entryAddAnswer.pack(pady=20)
    buttonAddAnswer = Button(frameAddition, text="Answer", bg="white", command=functionAddAnswer)
    buttonAddAnswer.pack()

    global answerMessage
    answerMessage = Label(frameAddition, text="", font=("Helvetica", 18), bg="white")
    answerMessage.pack(pady=40)
    


# Random States
def functionRandomStates():
    
    global our_states
    our_states = ['madhyapradesh', 'rajasthan', 'tamilnadu', 'uttarakhand', 'uttarpradesh']

    # Generate Random Number
    global rando
    rando = randint(0, len(our_states)-1)
    state = "States/"+our_states[rando]+".png"
    # Create our State Images
    global stateImage
    stateImage = ImageTk.PhotoImage(Image.open(state))
    showState.config(image = stateImage, bg="white")

    # showState = Label(frameState, image=stateImage)
    # showState.pack(pady=15)


# Crate a StateCapital Answer 
def functionStateCapitalAnswer():
    if radioCapital.get() == dictStateCapitals[answer]:
        response = "Correct! " + dictStateCapitals[answer] + " is the capital of " + answer
    else:
        response = "Incorrect! " + dictStateCapitals[answer] + " is the capital of " + answer
    labelCAnswer.config(text=response)

# Create a Answer Function
def functionCheckAnswer():
    answer1 = entryAnswer.get()
    answer = answer1.replace(" ", "")

    if answer.lower() == our_states[rando]:
        labelAnswer.config(text=answer1.title() + " is Correct")
    else:
        labelAnswer.config(text=answer1.title() + " is not Correct!!! " + our_states[rando].title() + " is Correct")
    
    # Clear Answer Input Entry
    entryAnswer.delete(0, 'end')
    functionRandomStates()


# Create State Flash Card Function
def functionState():
    #Hide Previous Frame
    hideAllFrames()
    frameState.pack(fill=BOTH, expand=1)
    # myLabel = Label(frameState, text="States").pack()

    """# Create a list of state name
    global our_states
    our_states = ['madhyapradesh', 'rajasthan', 'tamilnadu', 'uttarakhand', 'uttarpradesh']

    # Generate Random Number
    global rando
    rando = randint(0, len(our_states)-1)
    state = "States/"+our_states[rando]+".png"
    # Create our State Images
    global stateImage
    stateImage = ImageTk.PhotoImage(Image.open(state))"""

    global showState
    showState = Label(frameState)
    showState.pack(pady=15)
    functionRandomStates()

    # Create a Answer Entry
    global entryAnswer
    entryAnswer = Entry(frameState, font=('Helvetica', 18), bd=2)
    entryAnswer.pack(pady=10)

    # Create Button to randomize images
    buttonRando = Button(frameState, text="PASS", command=functionState)
    buttonRando.pack(pady=10)

    # Create a Button to Answer the Question
    buttonAnswer = Button(frameState, text="Answer", command=functionCheckAnswer)
    buttonAnswer.pack(pady=10)

    # Create a Label for Answer
    global labelAnswer
    labelAnswer = Label(frameState, text="", font=("Helvetica", 18), bg="white")
    labelAnswer.pack(pady=15)

# Create State Capitals Flash Card Function
def functionStateCapitals():
    # Hide Previous Frame
    hideAllFrames()
    frameStateCapitals.pack(fill=BOTH, expand=1)
    # myLabel = Label(frameStateCapitals, text="Capitals").pack()

    global showState
    showState = Label(frameStateCapitals)
    showState.pack(pady=15)


    global our_states
    our_states = ['madhyapradesh', 'rajasthan', 'tamilnadu', 'uttarakhand', 'uttarpradesh']

    global dictStateCapitals
    dictStateCapitals  = {
    'madhyapradesh': 'bhopal',
    'uttarakhand': 'dehradun',
    'uttarpradesh': 'lucknow',
    'rajasthan':'jaipur',
    'tamilnadu':'chennai'
                        }

    listAnswer = []
    count = 1
    global answer
    # Generate Three Random Capitals
    while count < 4:
        rando = randint(0, len(our_states)-1)
        # If First Selection, make it our answer
        if count == 1:
            answer = our_states[rando]
            global stateimage
            state = "States/" + our_states[rando] + ".png"
            stateimage = ImageTk.PhotoImage(Image.open(state))
            showState.config(image=stateimage)

        # Add our first selection to a new list
        listAnswer.append(our_states[rando])

        # Remove from old list
        our_states.remove(our_states[rando])

        # Shuffle original list
        random.shuffle(our_states)


        count += 1

    random.shuffle(listAnswer)
    global radioCapital
    radioCapital = StringVar()
    radioCapital.set(dictStateCapitals[listAnswer[0]])

    buttonRadioCapital1 = Radiobutton(frameStateCapitals, text=dictStateCapitals[listAnswer[0]].title(), variable=radioCapital, value=dictStateCapitals[listAnswer[0]]).pack()
    buttonRadioCapital2 = Radiobutton(frameStateCapitals, text=dictStateCapitals[listAnswer[1]].title(), variable=radioCapital, value=dictStateCapitals[listAnswer[1]]).pack()
    buttonRadioCapital3 = Radiobutton(frameStateCapitals, text=dictStateCapitals[listAnswer[2]].title(), variable=radioCapital, value=dictStateCapitals[listAnswer[2]]).pack()

    # Add a Pass Button
    buttonPass = Button(frameStateCapitals, text="pass", command=functionStateCapitals)
    buttonPass.pack(pady=15)

    # Add a Answer Button
    buttonCAnswer = Button(frameStateCapitals, text="Answer", command=functionStateCapitalAnswer)
    buttonCAnswer.pack(pady=10)

    # Add an Answer Label
    global labelCAnswer
    labelCAnswer = Label(frameStateCapitals, text="", font=("Helvetica", 18))
    labelCAnswer.pack(pady=15)
# Hide All Previous Frames
def hideAllFrames():

    # Loop thru all children and destroy in each frame
    for widget in frameState.winfo_children():
        widget.destroy()
    
    for widget in frameStateCapitals.winfo_children():
        widget.destroy()

    for widget in frameAddition.winfo_children():
        widget.destroy()

    frameAddition.pack_forget()
    frameState.pack_forget()
    frameStateCapitals.pack_forget()

# Create Our Menu
myMenu = Menu(root)
root.config(menu=myMenu)

# Menu Items - Geography 
menuGeography = Menu(myMenu)
myMenu.add_cascade(label="Geography", menu=menuGeography)
menuGeography.add_command(label="States", command=functionState)
menuGeography.add_command(label="States Capitals", command=functionStateCapitals)
menuGeography.add_separator()
menuGeography.add_command(label="Exit", command=root.quit)

# Menu Items - Maths
menuMaths = Menu(myMenu)
myMenu.add_cascade(label="Maths", menu=menuMaths)
menuMaths.add_command(label="Addition", command=functionAddition)

# Create Our Frame
frameState = Frame(root, height=500, width=500, bg="white")
frameStateCapitals = Frame(root, height=500, width=500)

# Crate Addition Frame
frameAddition = Frame(root, height=500, width=500, bg="white")


root.mainloop()