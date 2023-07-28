import tkinter as tk
from datetime import date



root = tk.Tk()
root.title('Date in Tkinter')
root.geometry('500x350')

panic = tk.Label(root, text="Don't Panic", font=("Helvetica", 42), bg="black", fg="green")
panic.pack(pady=20, ipadx=10, ipady=20)

# Get Date
today = date.today()

# Format Date
f_today = today.strftime("%A - %B %d, %Y ")

today_label = tk.Label(root, text=f"Today is {f_today}")
today_label.pack(pady=20)

# Countdown
days_in_year = 365
today_day_number = int(today.strftime("%j"))

# Calculate Left days in Year
left_days = days_in_year - today_day_number

countdown_label = tk.Label(root, text=f"There are Only {left_days} days \n Left in 2024", font=("Helvetica", 18))
countdown_label.pack(pady=20)



root.mainloop()