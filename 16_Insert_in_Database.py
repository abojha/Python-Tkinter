from tkinter import *
import sqlite3


root = Tk()


def submit():

    conn = sqlite3.connect('address_book.db')

    #Create cursor
    c = conn.cursor()

    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :zipcode)",
    {
        'f_name' : f_name.get(),
        'l_name' : l_name.get(),
        'address' : address_name.get(),
        'city' : city_name.get(),
        'zipcode' : zipcode_name.get()
    })
    conn.commit()
    conn.close()


    f_name.delete(0, END)
    l_name.delete(0, END)
    address_name.delete(0, END)
    city_name.delete(0, END)
    zipcode_name.delete(0, END)

f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)

address_name = Entry(root, width=30)
address_name.grid(row=2, column=1, padx=20)

city_name = Entry(root, width=30)
city_name.grid(row=3, column=1, padx=20)

zipcode_name = Entry(root, width=30)
zipcode_name.grid(row=4, column=1, padx=20)


#Create text area labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0)

l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)

address_name_label = Label(root, text="Address")
address_name_label.grid(row=2, column=0)

city_name_label = Label(root, text="City Name")
city_name_label.grid(row=3, column=0)

zipcode_name_label = Label(root, text="Zip Code")
zipcode_name_label.grid(row=4, column=0)

submit_btn = Button(root, text="Add button to Submit", command=submit)
submit_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


def query():
    conn = sqlite3.connect('address_book.db')

    #Create cursor
    c = conn.cursor()

    c.execute("SELECT *, oid FROM addresses")
    print(c.fetchall())

    

    conn.commit()

    conn.close()



query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


root.mainloop()