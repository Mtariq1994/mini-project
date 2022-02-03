def menu():
    print('Welcome to Cafe Leaf, here are your options:')
    print('0. Exit App')
    print('1. Go to Product Options Menu')
    print('2. Go to Courier Options Menu')

menu()
products_list = ['1. Sandwhiches', '2. Soups', '3. Snacks', '4. Bakery', '5. Hot Drinks', '6. Cold Drinks']

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
                for index,item in enumerate(products_list):
                    print(index,item)
            elif options_menu == 2:
                new_product = input('Please enter new product: ')
                products_list.append(new_product) #Here ive Gotten user input and appended product to product list
            elif options_menu == 3:
                remove_product = int(input('Which indexed item would you like to remove?: '))
                products_list.remove(products_list[remove_product])
                ###App is functioning! End of week1. 21/1/21
                ##COURIER
print(menu())
#menu()