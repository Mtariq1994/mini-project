import json
import csv
import pymysql
from order_list import orders_log
import os
from dotenv import load_dotenv

products_list_txt_file = open("products_list.txt", 'r+')#Files i will use
products_list_txt = products_list_txt_file.readlines() # do i need this? i dont get what its doing here
#new_product = products_list_txt_file
# Load environment variables from .env file
load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

###///////////////////////////////////////////FUNCTION LIST\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ 
#Connect to database function
def connect_to_db():
    connection = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    return connection
#Display products from mySQL Miniproject database 
def display_products():
                    connection = connect_to_db()
                    cursor = connection.cursor()
                    cursor.execute('SELECT * FROM products') # * denotes all from products
                    rows = cursor.fetchall()
                    for row in rows:
                        print(row)
##########
#Display courier from mySQL Miniproject database 
def display_courier():
                    connection = connect_to_db()
                    cursor = connection.cursor()
                    cursor.execute('SELECT * FROM courier')
                    rows = cursor.fetchall()
                    for row in rows:
                        print(row)


#Reading CSV files function
#Read CSV File
def read_csv(csv_file_name):
    data = []
    with open(csv_file_name, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
            #return data
    return data
###############
#Adding to Product CSV file function
def add_csv(open_file):
    #data = []     
    product_name = input("add product: ")
    product_price = float(input("Enter price: "))
    product_dictionary = {"product name":product_name, "product price":product_price}
    with open("products_list.csv", mode='a', newline='') as file:
        field_name = ["product name", "product price"]
        writer = csv.DictWriter(file,fieldnames=field_name, delimiter=',')
        writer.writerow(product_dictionary)
        #return data
#####
##Courier add function
def add_courier():
    data = [] #dont think this is needed    
    courier_name = input("Add Courier Name: ")
    courier_number = int(input("Enter Phone Number: "))
    courier_dictionary = {"courier":courier_name, "phone number":courier_number}
    with open("courier_list.csv", mode='a', newline='') as file:
        field_name = ["courier", "phone number"]
        writer = csv.DictWriter(file,fieldnames=field_name, delimiter=',')
        writer.writerow(courier_dictionary)
        return data
    ###
#Delete product function
def delete_product_csv():
    data = []
    del_prod = input('Enter the name of the product you want to delete: ')
    with open('products_list.csv', 'r') as f:
        deleting = f.readlines()
        prod_found = [x for x in deleting if x.split(',')[0].lower() == del_prod.lower()]
        if prod_found:
            print('Remove you product: {}'.format(del_prod))
            deleting.remove(prod_found[0])
            with open('products_list.csv', 'w') as f:
                f.write(''.join(deleting))
        else:
            print('Sorry! product "{}" not found.'.format(del_prod)) #this works but applies only to products and no index
    return data
####
#Delete courier function
def delete_courier_csv():
    data = []
    del_courier = input('Enter the name of the courier you want to delete: ')
    with open('courier_list.csv', 'r') as f:
        deleting = f.readlines()
        courier_found = [x for x in deleting if x.split(',')[0].lower() == del_courier.lower()]
        if courier_found:
            print('Remove you product: {}'.format(del_courier))
            deleting.remove(courier_found[0])
            with open('courier_list.csv', 'w') as f:
                f.write(''.join(deleting))
        else:
            print('Sorry! courier "{}" not found.'.format(del_courier)) #this works but applies only to products and no index
    return data
#Add order function CSV
def add_order_csv():      
    customer_name = input("add customer name: ")
    customer_address = input("what is their address?: ")
    customer_phone = input("what is their phone number?")
    for index,item in enumerate(couriers): 
                    print(index,item)#Shows courier for ease of choosing which one
    courier = input("What is Courier number?: ")
    status = input("what is their status?: ")
    order_dictionary = {"customer_name":customer_name, "customer_address": customer_address, "customer_phone": customer_phone, "courier": courier, "status": status}
    with open("order_list.csv", mode='a', newline='') as file:
        field_name = ["customer_name", "customer_address", "customer_phone", "courier", "status"]
        writer = csv.DictWriter(file,fieldnames=field_name, delimiter=',')
        writer.writerow(order_dictionary)
#########
#Update order Function CSV
def update_order_csv():
    status_change = ["preparing", "out-for-delivery", "delivered"]
    for index, order in enumerate(orders):
        print(index, order)

    chosen_order_index = int(input("pick an order: "))

    for index, status in enumerate(status_change):
        print(index, status)

    chosen_status_index = int(input("pick a status: "))

    orders[chosen_order_index]["status"] = status_change[chosen_status_index]

    with open('order_list.csv', 'w', newline='') as file:
        field_name =  ['customer_name', 'customer_address', 'customer_phone', 'courier', 'status']
        writer = csv.DictWriter(file,fieldnames=field_name, delimiter=',')
        writer.writeheader()
        writer.writerows(orders)
    
    return orders
###///////////////////////////////////////////FUNCTION LIST\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ 


##GLOBAL VARIABLES
products = read_csv('products_list.csv')
couriers = read_csv('courier_list.csv')
orders = read_csv('order_list.csv')
###////////////////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ 


courier_list = open("courier_list.txt", 'r+') #Files i will use
while (True):
    print('Welcome to Cafe Leaf, here are your options:')
    print('0. Exit App')
    print('1. Go to Product Options Menu')
    print('2. Go to Courier Options Menu')   
    print('3. Go to Order Options Menu')
    main_menu = int(input('Please select your option: '))
    if main_menu == 0:
        print('Exiting app...')
        break
###PRODUCTS MENU
    elif main_menu == 1:
        while (True):
            print("""
Welcome to Options menu, please select your option
-----------------------
0- Return to Main Menu
1 - Show Products 
2 - Add Products
3 - Remove Products
""")
            options_menu = int(input('Please select your option: '))
            if options_menu == 0:
                print('Returning to Main Menu...')
                break
            elif options_menu == 1:
                display_products() # With this function, im able to print all my products easily and neatly
#==== usable                           
                
            elif options_menu == 2: #Add new product
                    connection = connect_to_db()
                    cursor = connection.cursor()
                    display_products()#Function to display the products
                    add_product = input("Enter the name of the product: ")
                    add_price = input("Enter the price: ")
                    sql = "INSERT INTO products (name, price) VALUES (%s, %s)"
                    val = (add_product, add_price)
                    cursor.execute(sql, val)
                    product_dictionary = {"name":add_product, "price":add_price}
                    connection.commit() #this worked!
                    print("Here are your updated products",product_dictionary)
                    #Adds to my DataBase and saves!
            elif options_menu == 3: #REMOVE PRODUCTS
                
                    connection = connect_to_db()
                    cursor = connection.cursor() #always put my cursor on top
                    display_products()#Function to display the products
                    delete_ID = input("Enter ID of the product you wish to delete: ")
                    sql = f"DELETE FROM products WHERE id = {delete_ID} "#f is string interpolation, so i can use python within a string
                    cursor.execute(sql)
                    connection.commit()
                    print(cursor.rowcount, "product deleted")
###COURIER MENU
    elif main_menu == 2:
        while (True):
            print("""
Welcome to Courier Options menu, please select your option
-----------------------
0- Return to Main Menu
1 - Show Couriers
2 - Add Courier
3 - Remove Courier
""")
            courier_options_menu = int(input('Please select your option: '))
            if courier_options_menu == 0:
                print('Returning to Main Menu...')
                break ###working so far

            elif courier_options_menu == 1:
                display_courier() #Displays courier
            elif courier_options_menu == 2: #Add courier
                    connection = connect_to_db()
                    cursor = connection.cursor()
                    display_courier()#Function to display the products
                    new_courier = input("Enter the name of the courier: ")
                    add_phone = input("Enter their number: ")
                    sql = "INSERT INTO courier (name, phone_number) VALUES (%s, %s)"
                    val = (new_courier, add_phone)
                    cursor.execute(sql, val)
                    product_dictionary = {"name":new_courier, "price":add_phone}
                    connection.commit() #this worked!
                    print("Here is your updated list of couriers",product_dictionary)
                    #Adds to my DataBase and saves!
#####====================================================================================                
            elif courier_options_menu == 3: #Delete Courier
                    connection = connect_to_db()
                    cursor = connection.cursor() #always put my cursor on top
                    display_courier()#Function to display the products
                    delete_ID = input("Enter ID of the courier you wish to delete: ")
                    sql = f"DELETE FROM courier WHERE id = {delete_ID} "#f is string interpolation, so i can use python within a string
                    cursor.execute(sql)
                    connection.commit()
                    print(cursor.rowcount, "courier deleted")

###End of week 5, 22/2/22

#######===================================================================================


    elif main_menu == 3:
        while (True):
            print("""
Welcome to Orders Menu, please select your option
-----------------------
0- Return to Main Menu
1 - Show orders
2 - Create order
3 - Update order status 
""")

            order_options_menu = int(input('Please select your option: '))
            if order_options_menu == 0:
                print('Returning to Main Menu...')
                break ###working so far
            elif order_options_menu == 1:
                print(orders) ####CURRENT WORKING 17/2/22
            elif order_options_menu == 2:
                    add_order = add_order_csv() #add to csv
                    orders = read_csv('order_list.csv') # copy csv back into variable
                    print(orders)#print updated csv
                    print("order has been added") #ADD NEW ORDER
                    
# ##=========

            elif order_options_menu == 3: ###stuck here
                    new_orders_list = update_order_csv() #add to csv
                    orders = read_csv('order_list.csv') # copy csv back into variable
                    print(orders)#print updated csv
                    print("order has been added") #ADD NEW ORDER
#CURRENT WORKING 17/2/22, use reusable function and quickly refactor the rest of the code

##Week 4 is complete i can complete the next section as a stretch goal [read it from csv and save] and move on to databases
#See update_order_csv function and create a function using below
#==============
