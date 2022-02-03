print('Welcome to Cafe Leaf, here are your options:')
print('0. Exit App')
print('1. Go to Product Options Menu')
print('2. Go to Courier Options Menu')
# products_list = ['1. Sandwhiches', '2. Soups', '3. Snacks', '4. Bakery', '5. Hot Drinks', '6. Cold Drinks']
products_list_txt = open("products_list.txt", 'r+')
courier_list = ['1. Steve', '2. Tony', '3. Bruce', '4. Peter']
while (True):
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
                for index,item in enumerate(products_list_txt):
                    print(index,item)
            elif options_menu == 2:
                new_product = input('Please enter new product: ')
                products_list_txt.write(new_product)
                #Cant go back to displaying options menu, and seems to save product next time i run app???
                #products_list_txt.close
                #
                #f.write("Q.) \n")
                #f.close()
                #
                #
                #
                
            elif options_menu == 3:
                remove_product = int(input('Which indexed item would you like to remove?: '))
                products_list_txt.remove(products_list_txt[remove_product])
                ###App is functioning! End of week1. 21/1/21
#                 ##COURIER
#     elif main_menu == 2:
#         while (True):
#             print("""
# Welcome to Courier Options menu, please select your option
# -----------------------
# 0- Return to Main Menu
# 1 - Show Couriers
# 2 - Add Courier
# 3 - Remove Courier
# """)
#             courier_options_menu = int(input('Please select your option: '))
#             if courier_options_menu == 0:
#                 print('Returning to Main Menu...')
#                 break ###working so far
#             elif courier_options_menu == 1:
#                 for index,item in enumerate(courier_list):
#                     print(index,item)
#             elif courier_options_menu == 2:
#                 new_courier = input('Please enter name of new Courier: ')
#                 courier_list.append(new_courier)
#             elif courier_options_menu == 3:
#                 remove_courier = int(input('Which indexed Courier would you like to remove?: '))
#                 courier_list.remove(courier_list[remove_courier])
#                 ###I need to add something to print the main menu again>Ask for help