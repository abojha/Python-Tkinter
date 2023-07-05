import tkinter as tk



root = tk.Tk()
root.title('Text Box')
root.geometry('500x450')

# Create Clear Function
def clear():
    myText.delete(1.0, tk.END)

# Create Get Text Function
def getText():
    myLabel.config(text=myText.get(1.0, tk.END))


myText = tk.Text(root, width=40, height=10, font=("Helvetica", 16))
myText.pack(pady=20)

buttonFrame = tk.Frame(root)
buttonFrame.pack()

clearBtn = tk.Button(buttonFrame, text="Clear", command=clear)
clearBtn.grid(row=0, column=0)

getTextBtn = tk.Button(buttonFrame, text="Get Text", command=getText)
getTextBtn.grid(row=0, column=1)

myLabel = tk.Label(root, text="")
myLabel.pack(pady=20)

root.mainloop()