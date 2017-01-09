'''
Created on 2017/01/06

@author: yu-suke
'''
import sys
from myiterator.menu_item import MenuItem
from myiterator.diner_menu_iterator import DinerMenuIterator
from myiterator.menu import Menu


class DinerMenu(Menu):
    '''
    DinerMenu class
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.__MAX_ITEMS = 6
        self.__number_items = 0
        self.menu_items = {}
        self.add_item("vegetarian BLT",
                      "Sandwich sandwiched between lettuce and tomato and pseudo-bacon",
                      True, 2.99)
        self.add_item("BLT",
                      "Sandwich sandwiched between lettuce and tomato and bacon",
                      False, 2.99)

    def add_item(self, name: str, description: str,
                 vegetarian: True, price: float):
        if(self.__number_items >= self.__MAX_ITEMS):
            sys.stderr.write("sorry, menu items is full")
        else:
            menu_item = MenuItem(name, description, vegetarian, price)
            self.menu_items[self.__number_items.__str__()] = menu_item
            self.__number_items += 1

    # def get_menu_items(self):
    #    return self.menu_items

    def create_iterator(self):
        return DinerMenuIterator(self.menu_items)

if __name__ == "__main__":
    diner_menu = DinerMenu()
    for obj in diner_menu.create_iterator():
        print("name :{}\n{}\nvegetarian:{}\nprice:{}".format(
            obj.get_name(), obj.get_description(), obj.get_vegetarian(), obj.get_price()))
    diner_menu_iterator = diner_menu.create_iterator()
    print(diner_menu_iterator.__next__().get_name())
    print(diner_menu_iterator.__next__().get_name())
    print(diner_menu_iterator.__next__().get_name())
