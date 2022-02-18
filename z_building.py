
import csv
import numbers

from numpy import prod

# def update_order(orders):
#     for index, order in enumerate(orders):
#         print(index, order)

#     chosen_order_index = int(input("pick an order: "))

#     for index, status in enumerate(statuses):
#         print(index, status)

#     chosen_status_index = int(input("pick a status: "))

#     orders[chosen_order_index]["status"] = statuses[chosen_status_index]

#     return orders

# def update_product(orders):
#     for index, order in enumerate(orders):
#         print(index, order)

#     chosen_order_index = int(input("pick an order: "))

#     for index, status in enumerate(statuses):
#         print(index, status)

#     chosen_status_index = int(input("pick a status: "))

#     orders[chosen_order_index]["status"] = statuses[chosen_status_index]

#     return orders

#With the csv module you can iterate over the rows and
# access each one as a dict. As also noted here, the preferred way to update a file is by using temporary file.

# from tempfile import NamedTemporaryFile
# import shutil

# filename = 'products_list.csv'
# tempfile = NamedTemporaryFile(mode='w', delete=False)

# fields = ['Products', 'Price']

# with open(filename, 'r') as csvfile, tempfile:
#     reader = csv.DictReader(csvfile, fieldnames=fields)
#     writer = csv.DictWriter(tempfile, fieldnames=fields)
#     for new_product in reader:
#         if new_product['Products'] == str('Products'):
#             print('updating Products', row['Products'])
#             row['Name'], row['Course'], row['Year'] = stud_name, stud_course, stud_year
#         row = {'ID': row['ID'], 'Name': row['Name'], 'Course': row['Course'], 'Year': row['Year']}
#         writer.writerow(row)

# # shutil.move(tempfile.name, filename)
# def update_products():
#     with open('products_list.csv', mode='a+') as file:
#         fieldnames = ['Products', 'Price']
#         writer = csv.DictWriter(file, fieldnames=fieldnames)
#         writer.writeheader()
#         writer.writerow({
#         'Products': 'Jan',
#         'Price': 'Smith'
#         })
########################################
# def delete_csv():
#     data = []
#     del_prod = input('Enter the product you want to delete: ')
#     with open('products_list.csv', 'r') as f:
#         deleting = f.readlines()
#         prod_found = [x for x in deleting if x.split(',')[0].lower() == del_prod.lower()]
#         if prod_found:
#             print('Remove your product: {}'.format(del_prod))
#             deleting.remove(prod_found[0])
#             with open('products_list.csv', 'w') as f:
#                 f.write(''.join(deleting))
#         else:
#             print('Sorry! product "{}" not found.'.format(del_prod)) #this works but applies only to products and no index
#     return data
# ##
# del_products = delete_csv()
# print(del_products)
# print("Product has been deleted") #Deleting to CSV 

#=Question, Data does not update in app until i rerun it
# how can i include indexing here in csv?
###########################################################

##read csv should just be read csv instead of multiple functions
#convert couriers file to csv
#open with read_csv
#update function is needed, couriers,products orders etc should just be one function for csv files
#then use in all 3 categories
def add_order_csv():      
    customer_name = input("add product: ")
    address = input("Enter price: ")
    phone_number = input("what is their phone number?")
    for index,item in enumerate(couriers): 
                    print(index,item.strip())#Shows courier for choosing which one
    courier = input("What is Courier number?")
    order_dictionary = {"customer name":customer_name, "address": address, "phone_number": phone_number, "Courier": courier}
    with open("order_list.csv", mode='a', newline='') as file:
        field_name = ["Customer name", "address", "phone number", "courier"]
        writer = csv.DictWriter(file,fieldnames=field_name, delimiter=',')
        writer.writerow(order_dictionary)    
    
    
    
    
    
    
             
                customer_name = input("What is customer name?")
                address = input("what is their address?")
                phone_number = input("what is their phone number?")
                for index,item in enumerate(couriers): #Shows courier
                    print(index,item.strip())
                courier = input("What is Courier number?")
                #status = input("what is order status?")
                new_order= {
                    "customer_name": customer_name,
                    "customer_address": address,
                    "customer_phone": phone_number,
                    "courier": courier,
                    "status": "preparing"
                    }
                # orders.append(new_order)
                # new_order = orders#trying this
                # print(orders) #Adds to the order list but does not persist?
                new_order = orders
                orders = read_csv('order_list.csv')
                print(orders)
                
                
                #orders_log.append(new_order)
                #
               # print(orders_log)