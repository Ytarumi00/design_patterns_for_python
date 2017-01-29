'''
Created on 2017/01/29

@author: yu-suke
'''


class MenuComponent(object):
    '''
    MenuComponent class
    '''

    def __init__(self):
        '''
        Constructor
        '''

    def add(self, menu_component: MenuComponent):
        raise UserWarning("unsupported operation.")

    def remove(self, menu_component: MenuComponent):
        raise UserWarning("unsupported operation.")

    def get_child(self, i: int):
        raise UserWarning("unsupported operation.")

    def get_name(self):
        raise UserWarning("unsupported operation.")

    def get_description(self):
        raise UserWarning("unsupported operation.")

    def get_price(self):
        raise UserWarning("unsupported operation.")

    def is_vegetarian(self):
        raise UserWarning("unsupported operation.")

    def print(self):
        raise UserWarning("unsupported operation.")
