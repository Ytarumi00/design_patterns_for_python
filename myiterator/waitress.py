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
from myiterator.menu_component import MenuComponent


class Waitress(object):
    '''
    Waitress class
    '''

    def __init__(self, all_menus: MenuComponent):
        '''
        Constructor
        '''
        self.__all_menus = all_menus

    def display_menu(self):
        self.__all_menus.display()
