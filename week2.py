
products_list_txt_file = open("products_list.txt", 'r+')#Files i will use
products_list_txt = products_list_txt_file.readlines() # do i need this? i dont get what its doing here
#new_product = products_list_txt_file
courier_list = open("courier_list.txt", 'r+') #Files i will use
while (True):
    print('Welcome to Cafe Leaf, here are your options:')
    print('0. Exit App')
    print('1. Go to Product Options Menu')
    print('2. Go to Courier Options Menu')    
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
#categories for each product
