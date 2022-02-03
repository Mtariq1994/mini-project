
print('Welcome to the Cafe, here are your options:')
products_list = ['1. Sandwhiches', '2. Soups', '3. Snacks', '4. Bakery', '5. Hot Drinks', '6. Cold Drinks']
while (True): #to loop to main menu, so nothing breaks 
    main_menu = int(input("""
0 - Exit App
1 - Option Menu
"""))  
    if main_menu == 0:
        print('Exiting App...')
        break
    elif main_menu == 1:
        while True:
            menu_options = int(input("""
Option Menu
------------
0 - Main Menu
1 - Product List
"""))
            if menu_options == 0:
                break
            elif menu_options == 1:
                print(products_list)
                break
            