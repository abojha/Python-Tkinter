import tkinter as tk

splash_root = tk.Tk()
splash_root.title("Splash Screen")
splash_root.geometry("300x200")

splash_label = tk.Label(splash_root, text="Splash Screen", font=("Helvetica", 20))
splash_label.pack(pady=20)

def main():
    splash_root.destroy()
    root = tk.Tk()
    root.title('Splash Screen')
    root.geometry('500x550')

    main_label = tk.Label(root, text="Main Stream", font=("Helvetica", 20))
    main_label.pack(pady=20)

# Splash Screen Timer
splash_root.after(3000, main)

splash_root.mainloop()