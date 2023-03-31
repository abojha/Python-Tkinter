from tkinter import *
from PIL import ImageTk, Image
import mysql.connector
import csv
from tkinter import ttk



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
#
def functionAddToCart(result):
    with open("customer.csv", "a") as f:
        w = csv.writer(f, dialect='excel')
        for record in result:
            w.writerow(record)
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

# function to List all Customers
def functionListCustomers():
    ListCustomerQuery = Tk()
    ListCustomerQuery.title("List Of Customers")
    ListCustomerQuery.geometry("800x600")

    # Query the Database
    my_cursor.execute("SELECT * FROM customers")
    result = my_cursor.fetchall()
    for index, x in enumerate(result):
        num = 0
        for y in x:
            lookupLabel = Label(ListCustomerQuery, text=y)
            lookupLabel.grid(row=index, column=num)
            num+=1
    csv_button = Button(ListCustomerQuery, text="Add to CSV", command = lambda: functionAddToCart(result))
    csv_button.grid(row=index+1, column=0)

    

# Search Customers
def functionSearchCustomers():
    SearchCustomerQuery = Tk()
    SearchCustomerQuery.title("Search Customer")
    SearchCustomerQuery.geometry("1200x600")

    def functionUpdate():
        sql_command = """UPDATE customers SET  first_name = %s, last_name = %s, zipcode =  %s, price_paid = %s, user_id = %s, email = %s, address_1 = %s, address_2 = %s, city = %s, state = %s, country = %s, phone = %s, payment_method = %s, discount_code = %s WHERE user_id = %s"""

        first_name =  firstNameBox2.get()
        last_name =  lastNameBox2.get()
        address1 =  address1Box2.get()
        address2 =  address2Box2.get()
        city =  cityBox2.get()
        state = stateBox2.get()
        zipcode =  zipcodeBox2.get()
        country =  countryBox2.get()
        phone =  phoneBox2.get()
        email =  emailBox2.get()
        username =  usernameBox2.get()
        payment =  paymentMethodBox2.get()
        discount = discountCodeBox2.get()
        price =   PricePaidBox2.get() 

        inputs = (first_name, last_name, zipcode, price, username, email, address1, address2, city, state, country, phone, payment, discount, username)
        my_cursor.execute(sql_command, inputs)
        mydb.commit()

        SearchCustomerQuery.destroy()
    # Edit Now
    def functionEditNow(ref, index):

        sql2 = "SELECT * FROM customers WHERE user_id = %s"
        # sql = "SELECT * FROM customers WHERE last_name = %s"
        name2 = (ref, ) 
        result2 = my_cursor.execute(sql2, name2)
        result2 = my_cursor.fetchall()

        print(result2)
        index += 4
        # Create  Main Form to Enter Customer Data
        firstNameLabel2 = Label(SearchCustomerQuery, text="First Name").grid(row=index+1, column=0, sticky=W, padx=10)
        lastNameLabel2 = Label(SearchCustomerQuery, text="Last Name").grid(row=index+2, column=0, sticky=W, padx=10)
        address1Label2 = Label(SearchCustomerQuery, text="Address 1").grid(row=index+3, column=0, sticky=W, padx=10)
        address2Label2 = Label(SearchCustomerQuery, text="Address 2").grid(row=index+4, column=0, sticky=W, padx=10)
        cityLabel2 = Label(SearchCustomerQuery, text="City").grid(row=index+5, column=0, sticky=W, padx=10)
        stateLabel2 = Label(SearchCustomerQuery, text="State").grid(row=index+6, column=0, sticky=W, padx=10)
        zipcodeLabel2 = Label(SearchCustomerQuery, text="Zip Code").grid(row=index+7, column=0, sticky=W, padx=10)
        countryLabel2 = Label(SearchCustomerQuery, text="Country").grid(row=index+8, column=0, sticky=W, padx=10)
        phoneLabel2 = Label(SearchCustomerQuery, text="Phone").grid(row=index+9, column=0, sticky=W, padx=10)
        emailLabel2 = Label(SearchCustomerQuery, text="Email").grid(row=index+10, column=0, sticky=W, padx=10)
        usernameLabel2 = Label(SearchCustomerQuery, text="username").grid(row=index+11, column=0, sticky=W, padx=10)
        paymentMethodLabel2 = Label(SearchCustomerQuery, text="Payment Method").grid(row=index+12, column=0, sticky=W, padx=10)
        discountCodeLabel2 = Label(SearchCustomerQuery, text="Discount Method").grid(row=index+13, column=0, sticky=W, padx=10)
        pricePaidLabel2 = Label(SearchCustomerQuery, text="Price Paid").grid(row=index+14, column=0, sticky=W, padx=10)

        # Create Entry Box
        global firstNameBox2
        firstNameBox2 = Entry(SearchCustomerQuery)
        firstNameBox2.grid(row=index+1, column=1, pady=5)
        firstNameBox2.insert(0, result2[0][0])

        global lastNameBox2
        lastNameBox2 = Entry(SearchCustomerQuery)
        lastNameBox2.grid(row=index+2, column=1, pady=5)
        lastNameBox2.insert(0, result2[0][1])

        global address1Box2
        address1Box2 = Entry(SearchCustomerQuery)
        address1Box2.grid(row=index+3, column=1, pady=5)
        address1Box2.insert(0, result2[0][6])

        global address2Box2
        address2Box2 = Entry(SearchCustomerQuery)
        address2Box2.grid(row=index+4, column=1, pady=5)
        address2Box2.insert(0, result2[0][7])

        global cityBox2
        cityBox2 = Entry(SearchCustomerQuery)
        cityBox2.grid(row=index+5, column=1, pady=5)
        cityBox2.insert(0, result2[0][8])

        global stateBox2
        stateBox2 = Entry(SearchCustomerQuery)
        stateBox2.grid(row=index+6, column=1, pady=5)
        stateBox2.insert(0, result2[0][9])

        global zipcodeBox2
        zipcodeBox2 = Entry(SearchCustomerQuery)
        zipcodeBox2.grid(row=index+7, column=1, pady=5)
        zipcodeBox2.insert(0, result2[0][2])
        
        global countryBox2
        countryBox2 = Entry(SearchCustomerQuery)
        countryBox2.grid(row=index+8, column=1, pady=5)
        countryBox2.insert(0, result2[0][10])

        global  phoneBox2
        phoneBox2 = Entry(SearchCustomerQuery)
        phoneBox2.grid(row=index+9, column=1, pady=5)
        phoneBox2.insert(0, result2[0][11])

        global emailBox2
        emailBox2 = Entry(SearchCustomerQuery)
        emailBox2.grid(row=index+10, column=1, pady=5)
        emailBox2.insert(0, result2[0][5])

        global usernameBox2
        usernameBox2 = Entry(SearchCustomerQuery)
        usernameBox2.grid(row=index+11, column=1, pady=5)
        usernameBox2.insert(0, result2[0][4])

        global paymentMethodBox2
        paymentMethodBox2 = Entry(SearchCustomerQuery)
        paymentMethodBox2.grid(row=index+12, column=1, pady=5)
        paymentMethodBox2.insert(0, result2[0][12])

        global discountCodeBox2
        discountCodeBox2 = Entry(SearchCustomerQuery)
        discountCodeBox2.grid(row=index+13, column=1, pady=5)
        discountCodeBox2.insert(0, result2[0][13])

        global  PricePaidBox2
        PricePaidBox2 = Entry(SearchCustomerQuery)
        PricePaidBox2.grid(row=index+14, column=1, pady=5)
        PricePaidBox2.insert(0, result2[0][3])

        buttonSaveRecord = Button(SearchCustomerQuery, text="Update Record", command=functionUpdate)
        buttonSaveRecord.grid(row = index+15, column=0, padx=10)


    def functionSearchNow():
        selected = drop.get()
        sql = ""
        if selected == "Search by ...":
            test = Label(SearchCustomerQuery, text="Hey you forgot to pick a drop down selection")
            test.grid(row=3, column=0)
        if selected == "Last Name":
            sql = "SELECT * FROM customers WHERE last_name = %s"
        if selected == "Email Address":
            sql = "SELECT * FROM customers WHERE email = %s"
        if selected == "Customer ID":
            sql = "SELECT * FROM customers WHERE user_id = %s"

        searched = EntrySearchBox.get()
        # sql = "SELECT * FROM customers WHERE last_name = %s"
        name = (searched, ) 
        result = my_cursor.execute(sql, name)
        result = my_cursor.fetchall()

        if not result:
            result = "Record Not Found ... "

        for index, x in enumerate(result):
            num = 0
            id_reference = str(x[4])
            editButton = Button(SearchCustomerQuery, text="Edit" + id_reference, command=lambda: functionEditNow(id_reference, index))
            editButton.grid(row=index+3, column=num)
            for y in x:
                labelSearched = Label(SearchCustomerQuery, text=y)
                labelSearched.grid(row=index+3, column=num+1)
                num+=1

    # Entry Box to Search Customer
    EntrySearchBox = Entry(SearchCustomerQuery)
    EntrySearchBox.grid(row=0, column=1, padx=10, pady=10)

    # Label Box to Search to Customer
    labelSearch = Label(SearchCustomerQuery, text="Search")
    labelSearch.grid(row=0, column=0, padx=10, pady=10)

    # Search Button
    buttonSearch = Button(SearchCustomerQuery, text="Search Now", command=functionSearchNow)
    buttonSearch.grid(row=1, column=0, padx=10)

    # Drop Down Box
    drop = ttk.Combobox(SearchCustomerQuery, value=["Search by ...", "Last Name", "Email Address","Customer ID"])
    drop.current(0)
    drop.grid(row=0, column=2)



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

# list customers Button
listCustomerButton = Button(root, text = "Customers", command=functionListCustomers)
listCustomerButton.grid(row=16, column=0, sticky=W, padx=10)

# Search Customer Button
searchCustomerButton = Button(root, text = "Search/Edit", command=functionSearchCustomers)
searchCustomerButton.grid(row=16, column=1, sticky=W, padx=10)


root.mainloop()