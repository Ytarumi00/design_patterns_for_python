'''
Created on 2017/01/09

@author: yu-suke
'''
from myiterator.pancake_house_menu import PancakeHouseMenu
from myiterator.diner_menu import DinerMenu
from myiterator.iterator import Iterator
from myiterator.menu_item import MenuItem


class Waitress(object):
    '''
    Waitress class
    '''

    def __init__(self, pancake_house_menu: PancakeHouseMenu,
                 diner_menu: DinerMenu):
        '''
        Constructor
        '''
        self.pancake_house_menu = pancake_house_menu
        self.diner_menu = diner_menu

    def display_menu(self):
        pancake_iterator = self.pancake_house_menu.create_iterator()
        diner_menu = self.diner_menu.create_iterator()
        print("breakfast menu\n")
        self.print_menu(pancake_iterator)
        print("diner menu\n")
        self.print_menu(diner_menu)

    def print_menu(self, iterator: Iterator):
        while(iterator.has_next()):
            menu_item = iterator.next()
            print("{}\t{} -- {}\n".format(menu_item.get_name(),
                                          menu_item.get_price(),
                                          menu_item.get_description()))

if __name__ == "__main__":
    pancake_house_menu = PancakeHouseMenu()
    diner_menu = DinerMenu()

    waitress = Waitress(pancake_house_menu, diner_menu)

    waitress.display_menu()
