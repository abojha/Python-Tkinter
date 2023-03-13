from tkinter import *
from PIL import ImageTk, Image
import mysql.connector



root = Tk()
root.title('CRM Tools')
root.geometry('400x600')

# Connect to MySQL
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "abhay123",
    database = "binarydose"
)

#check to see if connection to MySQL was created
# print(mydb)

# Create a cursor and initialize it
my_cursor = mydb.cursor()

# Create Database
# my_cursor.execute("CREATE DATABASE binarydose")

# Test to see if database was created
# my_cursor.execute("SHOW DATABASES")
# for db in my_cursor:
#     print(db)

# Drop Table
# my_cursor.execute("DROP TABLE customer")

# # Create a table
my_cursor.execute("CREATE TABLE  IF NOT EXISTS customers (first_name VARCHAR(255),\
        last_name VARCHAR(255),\
        zipcode int(10),\
        price_paid DECIMAL(10, 2),\
        user_id INT AUTO_INCREMENT PRIMARY KEY)")



# # Alter Table
'''
my_cursor.execute("ALTER TABLE customers ADD (\
        email VARCHAR(255),\
        address_1 VARCHAR(255),\
        address_2 VARCHAR(255),\
        city VARCHAR(50),\
        state VARCHAR(50),\
        country VARCHAR(255),\
        phone VARCHAR(255),\
        payment_method VARCHAR(50 ),\
        discount_code VARCHAR(255))")
'''

# # Show Table
# my_cursor.execute("SELECT * FROM customers")
# # print(my_cursor.description)
# for thing in my_cursor.description:
#     print(thing)

# Functions
# function to clear all fields
def functionClearFields():
    firstNameBox.delete(0, END)
    lastNameBox.delete(0, END)
    address1Box.delete(0, END)
    address2Box.delete(0, END)
    cityBox.delete(0, END)
    stateBox.delete(0, END)
    zipcodeBox.delete(0, END)
    countryBox.delete(0, END)
    phoneBox.delete(0, END)
    emailBox.delete(0, END)
    usernameBox.delete(0, END)
    paymentMethodBox.delete(0, END)
    discountCodeBox.delete(0, END)
    PricePaidBox.delete(0, END)

# Submit customer to Database
def functionAddCustomer():
    sqlCommand = "INSERT INTO customers (first_name, last_name,  zipcode, price_paid, user_id, email, address_1, address_2, city, state, country, phone, payment_method, discount_code) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    values = (firstNameBox.get(), lastNameBox.get(), zipcodeBox.get(), PricePaidBox.get(), usernameBox.get(), emailBox.get(), address1Box.get(), address2Box.get(), cityBox.get(), stateBox.get(), countryBox.get(), phoneBox.get(), paymentMethodBox.get(), discountCodeBox.get())

    my_cursor.execute(sqlCommand, values)

    #Commit the changes to the database
    mydb.commit()
    functionClearFields()


# Create A Label
title_label = Label(root, text="Binary Dose Customer Database", font=("Helvetica", 16))
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# Create  Main Form to Enter Customer Data
firstNameLabel = Label(root, text="First Name").grid(row=1, column=0, sticky=W, padx=10)
lastNameLabel = Label(root, text="Last Name").grid(row=2, column=0, sticky=W, padx=10)
address1Label = Label(root, text="Address 1").grid(row=3, column=0, sticky=W, padx=10)
address2Label = Label(root, text="Address 2").grid(row=4, column=0, sticky=W, padx=10)
cityLabel = Label(root, text="City").grid(row=5, column=0, sticky=W, padx=10)
stateLabel = Label(root, text="State").grid(row=6, column=0, sticky=W, padx=10)
zipcodeLabel = Label(root, text="Zip Code").grid(row=7, column=0, sticky=W, padx=10)
countryLabel = Label(root, text="Country").grid(row=8, column=0, sticky=W, padx=10)
phoneLabel = Label(root, text="Phone").grid(row=9, column=0, sticky=W, padx=10)
emailLabel = Label(root, text="Email").grid(row=10, column=0, sticky=W, padx=10)
usernameLabel = Label(root, text="username").grid(row=11, column=0, sticky=W, padx=10)
paymentMethodLabel = Label(root, text="Payment Method").grid(row=12, column=0, sticky=W, padx=10)
discountCodeLabel = Label(root, text="Discount Method").grid(row=13, column=0, sticky=W, padx=10)
pricePaidLabel = Label(root, text="Price Paid").grid(row=14, column=0, sticky=W, padx=10)

# Create Entry Box
firstNameBox = Entry(root)
firstNameBox.grid(row=1, column=1, pady=5)

lastNameBox = Entry(root)
lastNameBox.grid(row=2, column=1, pady=5)

address1Box = Entry(root)
address1Box.grid(row=3, column=1, pady=5)

address2Box = Entry(root)
address2Box.grid(row=4, column=1, pady=5)

cityBox = Entry(root)
cityBox.grid(row=5, column=1, pady=5)

stateBox = Entry(root)
stateBox.grid(row=6, column=1, pady=5)

zipcodeBox = Entry(root)
zipcodeBox.grid(row=7, column=1, pady=5)

countryBox = Entry(root)
countryBox.grid(row=8, column=1, pady=5)

phoneBox = Entry(root)
phoneBox.grid(row=9, column=1, pady=5)

emailBox = Entry(root)
emailBox.grid(row=10, column=1, pady=5)

usernameBox = Entry(root)
usernameBox.grid(row=11, column=1, pady=5)

paymentMethodBox = Entry(root)
paymentMethodBox.grid(row=12, column=1, pady=5)

discountCodeBox = Entry(root)
discountCodeBox.grid(row=13, column=1, pady=5)

PricePaidBox = Entry(root)
PricePaidBox.grid(row=14, column=1, pady=5)

# Create Buttons
addCustomerButton = Button(root, text="Add Customer To Database", command=functionAddCustomer)
addCustomerButton.grid(row=15, column=0, padx=10, pady=10)

clearFieldsButton = Button(root, text="Clear Fields",command=functionClearFields)
clearFieldsButton.grid(row=15, column=1)

my_cursor.execute("SELECT * FROM customers")
result = my_cursor.fetchall()
for x in result:
    print(x)
root.mainloop()