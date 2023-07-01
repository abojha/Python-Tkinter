from tkinter import *

root = Tk()
root.title("Panned Window")
root.geometry("400x400")


#panels
panel_1 = PanedWindow(bd=4, relief="sunken", bg="red")
panel_1.pack(fill=BOTH, expand=1)

left_label = Label(panel_1, text="Left Pannel")
panel_1.add(left_label)

# Create a second panel
panel_2 = PanedWindow(panel_1,orient=VERTICAL,bd=4, relief="sunken", bg="blue")
panel_1.add(panel_2)

top = Label(panel_2, text="Top Pannel")
panel_2.add(top)

bottom = Label(panel_2, text="Bottom Pannel")
panel_2.add(bottom)

root.mainloop()