'''
Created on 2017/01/29

@author: yu-suke
'''
from myiterator.menu import Menu
from myiterator.menu_item import MenuItem


class CafeMenu(Menu):
    '''
    cafeMunu class
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.menu_items = {}
        self.add_item(
            "vegetable bugger and potato",
            "A vegetable vagger with lettuce and tomato sandwiched in whole wheat bread",
            True, 3.99)
        self.add_item("Today's soup",
                      "Today's soup with salad",
                      True, 3.69)

    def add_item(self, name: str, description: str,
                 vegetarian: bool, price: float):
        menu_item = MenuItem(name, description,
                             vegetarian, price)
        self.menu_items[name] = menu_item

    def create_iterator(self):
        return self.menu_items.values()


if __name__ == "__main__":
    cafe_menu = CafeMenu()
    for menu_item in cafe_menu.create_iterator():
        print(menu_item)
        print(menu_item.get_name())
