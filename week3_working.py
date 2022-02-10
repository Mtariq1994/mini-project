from ctypes import addressof
import json
from turtle import update
from order_list import orders_log
products_list_txt_file = open("products_list.txt", 'r+')#Files i will use
products_list_txt = products_list_txt_file.readlines() # do i need this? i dont get what its doing here
#new_product = products_list_txt_file
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
                with open("products_list.txt", 'r+') as products_list_txt_file: 
                    products_list_txt = products_list_txt_file.readlines()
                for index,item in enumerate(products_list_txt): ## VIEW PRODUCT
                    print(index,item.strip()) #STRIP got ride of the extra spacing per item
                    ##########################################################
                    
                    #products_list_txt_file = open("products_list.txt", 'r+')
#products_list_txt = products_list_txt_file.readlines()
            elif options_menu == 2:
                new_product_input = input('Please enter a new product: ')
                with open('products_list.txt', 'a+') as open_file:
                    open_file.write(new_product_input + '\n') ###UPDATING PRODUCT

            elif options_menu == 3:
                remove_product = int(input('Which indexed item would you like to remove?: '))
                products_list_txt.remove(products_list_txt[remove_product])
                with open('products_list.txt', 'w') as new_products_list_txt:
                    for product_name in products_list_txt:
                        new_products_list_txt.write(product_name) ###REMOVE PRODUCT
                ###open_file.write(new_product_input + '\n') REFERENCE to fix line above
                ###App is functioning! End of week1. 21/1/21

                ###COURIER
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
                with open('courier_list.txt', 'r+') as courier_list_txt_file:
                    courier_list_txt = courier_list_txt_file.readlines()
                for index,item in enumerate(courier_list_txt):
                    print(index,item.strip())       #SHOW COURIER    
            
            elif courier_options_menu == 2:
                new_courier_input = input('Please enter name of new Courier: ')
                with open ('courier_list.txt', 'a+') as open_file:
                    open_file.write(new_courier_input + '\n')        ##ADD COURIER

            elif courier_options_menu == 3:
                remove_product = int(input('Which indexed item would you like to remove?: '))
                courier_list_txt.remove(courier_list_txt[remove_product])
                with open('courier_list.txt', 'w') as new_courier_lists_txt:
                    for courier_name in courier_list_txt:
                        new_courier_lists_txt.write(courier_name) ## REMOVE COURIER

            #######CURRENT working upto here 28/1/21
                            ###App is functioning! End of week2. 27/1/21
                                            ###Week 2: I updated products list which now saves and can be used and updated, need to do same for courier
#Would creating a function for menu be easier?
#Look at notepad for things to add, definetly want to investigate OS and time?
#categories for each product #####################WEEK 3####################################################
#             orders = {
#     #key #value
# "customer_name": "Tony",
# "customer_address": "Avengers Tower, 5th Street, NYC, WH1 2ER",
# "customer_phone": "0789887334",
# "courier": 1,
# "status": "preparing"
# }
# for key, value in orders.items():
#     print(key, ' : ',value)


    elif main_menu == 3:
        while (True):
            print("""
Welcome to Orders Menu, please select your option
-----------------------
0- Return to Main Menu
1 - Show orders
2 - Create order
3 - Update order 
4 - Update existing order
5 - Delete order
""")

            order_options_menu = int(input('Please select your option: '))
            if order_options_menu == 0:
                print('Returning to Main Menu...')
                break ###working so far
            elif order_options_menu == 1: ###Stuck here
            #     for key, value in orders_log.items():
            #         print(key, ' : ',value)  
            # # #works but doesnt print in seperate lines
            
                # with open('order_list.py', 'r+') as orders_list: #not sure need
                #     order_read = orders_list.readlines() #not sure need, already imported order_list
                for order in orders_log:
                    #print(order.get('customer_name'))  ###Print manually whatever i want if i dont want brackets.  
                    print(json.dumps(order, sort_keys=False, indent=2, default=str))
                    
                    #print(json.dumps(orders_log, sort_keys=True, indent=2, default=str))
                        #second option of menu
                        #to add a new order: create a dictionary and append to orders log 
                        #  orders_log.append(new_orders_dictionary) 
                        ##alex notes these few lines
                        #research how to add dictionary to a list with input python
            elif order_options_menu == 2:
               
                customer_name = input("What is customer name?")
                address = input("what is their address?")
                phone_number = input("what is their phone number?")
                for index,item in enumerate(courier_list): #Shows courier
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
                orders_log.append(new_order)
                
                print(orders_log) ##Review mini project and see whats next
#                ##=========

            elif order_options_menu == 3:
                
                #print("select index of order you would you like to update?")
                for index,item in enumerate(orders_log):
                    #print(index,item.strip())
                    print(index,item)
                chosen_order = int(input('Which order status would you like to update?'))
                new_status = input('enter new status')
                
                orders_log[chosen_order]['status'] = new_status ##So i open the part of the dictionary i want and i update its key

            elif order_options_menu == 4: #update existing order
                for index,item in enumerate(orders_log):
                    print(index,item) 
                indexed_order = int(input('Which order would you like to update?'))
                
                new_name = input('What do you want to change the name to? (blank for no change): ')
                new_address = input('What do you want to change the address to? (blank for no change): ')
                new_number = input('what do you want to change the number to? (blank for no change): ')
                for index,item in enumerate(courier_list):
                    print(index,item)
                new_courier = input('what do you want to change the courier to? (blank for no change): ')
                if new_name == '':
                    pass
                else:
                    orders_log[indexed_order]['customer_name'] = new_name
                if new_address =='':
                    pass
                else: 
                    orders_log[indexed_order]['customer_address'] = new_address
                if new_number == '':
                    pass
                else:
                    orders_log[indexed_order]['customer_phone'] = new_number
                if new_courier == '':
                    pass
                else:
                    orders_log[indexed_order]['courier'] = new_courier
                print('Here is your new list of orders')
                print(orders_log)        
            elif order_options_menu == 5:
                for index,item in enumerate(orders_log):
                    #print(index,item.strip())
                    print(index,item)    
                delete_order = int(input('Which order would you like to delete?'))
                del orders_log[delete_order]
                #########WEEK 3 COMPLETE 10/2/22
                #Have not persisted update orders section 
                # Have not done any unit testing
                #week4:
                #writing to csv, everywhere ive used txt files update to csv
                #