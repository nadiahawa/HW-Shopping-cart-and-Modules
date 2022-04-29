# OG

# def check_shopping_cart():
#     print('your shopping cart consists of: ' )
# def add_items(item):
#     empty_cart = empty_cart.append(item)
#     print(f'{item} has been placed in cart!')
# def remove_item(item):
#     empty_cart = empty_cart.pop(item)
#     print(f'{item} has been removed from cart.')
# def quit_cart():
#      print('Thanks for shopping with us!')

# while True:
#     response = input('Welcome to shop mart! How can we help you today? Check shopping cart [check] Add Items [add] Remove Item [remove] Leave and quit[quit]')
#     if response.lower() == 'quit':
#         quit()
#         break
#     elif response.lower() == 'check':
#         check_shopping_cart()
#     elif response.lower() == 'add':
#         item = input('what would you like to add? ')
#         if item == "":
#             add_items(item)


# def add_item(the_cart):
#     item = input('What would you like to add to your cart?').title()
#     the_cart.append(item)








def shopping_cart():
    the_cart = []

    while True:
        response = input('Welcome to shop mart! How can we help you today? Check shopping cart [check] Add Items [add] Remove Item [remove] Leave and quit[quit]').lower()
        if response == 'check':
            print(f'Here is the_cart: {the_cart}.')
        elif response == 'quit':
            print(f'Thank you for shopping with us today, here is your final order: {the_cart}.')
            break
        elif response == 'add':
            item = input('What would you like to add to your cart?').title()
            the_cart.append(item)
        elif response == 'remove':
            item = input('What item would you like to remove?').title()
            the_cart.remove(item)
        else:
            print('Please select a valid option listed.')
shopping_cart()