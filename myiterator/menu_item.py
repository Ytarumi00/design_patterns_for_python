'''
Created on 2017/01/06

@author: yu-suke
'''
from myiterator.menu_component import MenuComponent


class MenuItem(MenuComponent):
    '''
    MenuItem class
    '''

    def __init__(self, name, description, vegetarian, price):
        '''
        Constructor
        '''
        self.name = name
        self.description = description
        self.vegetarian = vegetarian
        self.price = price

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_vegetarian(self):
        return self.vegetarian

    def get_price(self):
        return self.price

    def display(self):
        if(self.vegetarian is True):
            print(" {}(v), {}\n--{}".
                  format(self.name, self.price, self.description))
        else:
            print(" {}, {}\n--{}".
                  format(self.name, self.price, self.description))
