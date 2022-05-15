print("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
""")
items = ('Wings', 'Cookies', 'Spring Rolls')
quantity = 0
menu = dict.fromkeys(items, quantity)
order = input('> ')
while order != 'quit':
 if order in menu.keys():
    x = menu.get(order)
    x = x+1
    menu.update({order:x})
    print("** " + str(x) + " order of " + order + " have been added to your meal **")
    order = input('> ')
 elif order not in menu.keys():
    print("Item not in menu, Try Again")
    order = input('> ')
else:
    exit()