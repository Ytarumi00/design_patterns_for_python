'''
Created on 2017/01/09

@author: yu-suke
'''
from myiterator.pancake_house_menu import PancakeHouseMenu
from myiterator.diner_menu import DinerMenu
from myiterator.iterator import Iterator
from myiterator.menu_item import MenuItem
from myiterator.menu import Menu
from myiterator.cafe_menu import CafeMenu


class Waitress(object):
    '''
    Waitress class
    '''

    def __init__(self, menus: list):
        '''
        Constructor
        '''
        self.__menus = menus

    def display_menu(self):
        for menu in self.__menus:
            self.print_menu(menu)

    def print_menu(self, iterator: Iterator):
        for menu_item in iterator:
            print("{}\t{} -- {}\n".format(menu_item.get_name(),
                                          menu_item.get_price(),
                                          menu_item.get_description()))

if __name__ == "__main__":
    pancake_house_menu = PancakeHouseMenu()
    diner_menu = DinerMenu()
    cafe_menu = CafeMenu()
    menus = [pancake_house_menu.create_iterator(),
             diner_menu.create_iterator(),
             cafe_menu.create_iterator()]

    waitress = Waitress(menus)

    waitress.display_menu()
