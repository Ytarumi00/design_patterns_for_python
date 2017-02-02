'''
Created on 2017/01/29

@author: yu-suke
'''

from myiterator.menu import Menu
from myiterator.menu_item import MenuItem
from myiterator.waitress import Waitress


class MenuTestDriver(object):
    '''
    Driver for test menu
    '''

    def __init__(self):
        '''
        Constructor
        '''

    pancake_house_menu = Menu("Pancake house menu", "breakfirst")
    diner_menu = Menu("diner menu", "lunch")
    cafe_menu = Menu("cafe menu", "dinner")
    dessert_nenu = Menu("dessert_menu", "dessert")

    all_menus = Menu("all menus", "menu with all integrated")

    all_menus.add(pancake_house_menu)
    all_menus.add(diner_menu)
    all_menus.add(cafe_menu)

    pancake_house_menu.add(MenuItem("K&B pancake breakfast",
                                    "pancake with scrambled egg and a toast",
                                    True, 2.99))
    pancake_house_menu.add(MenuItem("basic pancake breakfast",
                                    "pancake with fried egg and a sausage",
                                    True, 3.49))

    diner_menu.add(MenuItem("vegetarian BLT",
                            "Sandwich sandwiched between lettuce and tomato and pseudo-bacon",
                            True, 2.99))
    diner_menu.add(MenuItem("BLT",
                            "Sandwich sandwiched between lettuce and tomato and bacon",
                            False, 2.99))

    cafe_menu.add(MenuItem("vegetable bugger and potato",
                           "A vegetable vagger with lettuce and tomato sandwiched in whole wheat bread",
                           True, 3.99))
    cafe_menu.add(MenuItem("Today's soup",
                           "Today's soup with salad",
                           True, 3.69))

    diner_menu.add(dessert_nenu)

    dessert_nenu.add(MenuItem("apple pie",
                              "Pie of flacked dought with vanilla ice cream",
                              True,
                              1.59))

    waitress = Waitress(all_menus)

    waitress.display_menu()
    print("\n\n")
    waitress.display_vegetarian_menu()
