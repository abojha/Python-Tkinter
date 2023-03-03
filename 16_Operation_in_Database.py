from tkinter import *
import sqlite3


root = Tk()


def submit():

    #connect to database
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

#Text Boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10,0))

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)

address_name = Entry(root, width=30)
address_name.grid(row=2, column=1, padx=20)

city_name = Entry(root, width=30)
city_name.grid(row=3, column=1, padx=20)

zipcode_name = Entry(root, width=30)
zipcode_name.grid(row=4, column=1, padx=20)

delete_record = Entry(root, width=30)
delete_record.grid(row=8, column=1, padx=20)


#Create text area labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0, pady=(10,0))

l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)

address_name_label = Label(root, text="Address")
address_name_label.grid(row=2, column=0)

city_name_label = Label(root, text="City Name")
city_name_label.grid(row=3, column=0)

zipcode_name_label = Label(root, text="Zip Code")
zipcode_name_label.grid(row=4, column=0)

delete_record_label = Label(root, text="Delete ID")
delete_record_label.grid(row=8, column=0)

submit_btn = Button(root, text="Add button to Submit", command=submit)
submit_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


#Show data from database
def query():

    #connect to database
    conn = sqlite3.connect('address_book.db')

    #Create cursor0
    c = conn.cursor()

    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()

    #Loop thu results
    print_records = ''
    for record in records:
        print_records += str(record[0] + " " + str(record[1]) + " " + "\t" + str(record[5]) + "\n")

    query_label = Label(root, text=print_records)
    query_label.grid(row=10, column=0, columnspan=2)

    
    #Commit Changes
    conn.commit()

    #close connections
    conn.close()

#Create function to Delete a Record
def delrecord():
    #connect to database
    conn = sqlite3.connect('address_book.db')

    #Create cursor0
    c = conn.cursor()

    #DELETE RECORD
    c.execute("DELETE FROM addresses WHERE oid = " + delete_record.get())

    delete_record.delete(0, END)


    #Commit Changes
    conn.commit()
    #close connections
    conn.close()



query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


#Create a deletebutton
delete_btn = Button(root, text="Delete Record", command=delrecord)
delete_btn.grid(row=9, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

root.mainloop()