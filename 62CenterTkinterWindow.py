import tkinter as tk



root = tk.Tk()
root.title('Center Tkinter Window')

# Designate Height and Width of our app
app_width = 500
app_height = 500

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width/2) - (app_width/2)
y = (screen_height/2) - (app_height/2)
root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')


my_label = tk.Label(root, text=f'Width:{screen_width} Height:{screen_height}')
my_label.pack(pady=20)
root.mainloop()