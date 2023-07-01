from tkinter import *
import sqlite3


root = Tk()



# Create a database or connect to one
conn = sqlite3.connect('address_book.db')

#Create cursor
c = conn.cursor()

# Create table
c.execute("""CREATE TABLE addresses (
    first_name text, 
    last_name text,
    address text,
    city text,
    zipcode integer)""")



# Commit changes
conn.commit()



#close
conn.close()




root.mainloop()