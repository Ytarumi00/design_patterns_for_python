'''
Created on 2017/01/09

@author: yu-suke
'''
from abc import ABCMeta, abstractmethod
from myiterator.menu_component import MenuComponent


class Menu(MenuComponent, metaclass=ABCMeta):
    '''
    Menu class
    '''

    def __init__(self, name: str, description: str):
        '''
        Constructor
        '''
        self.menu_components = []
        self.name = name
        self.description = description

    def add(self, menu_component: MenuComponent):
        self.menu_components.append(menu_component)

    def remove(self, menu_component: MenuComponent):
        self.menu_components.remove(menu_component)

    def get_child(self, i: int):
        return self.menu_components[i]

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def display(self):
        print("\n{},{}\n-----------------".format(self.name, self.description))

        for menu_component in self.menu_components:
            menu_component.display()
