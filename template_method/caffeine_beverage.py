'''
Created on 2016/12/27

@author: yu-suke
'''
from abc import ABCMeta, abstractmethod


class CaffeineBeverage(metaclass=ABCMeta):

    '''
    CaffeineBeverage
    '''

    def prepare_recipe(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    @abstractmethod
    def brew(self):
        pass

    @abstractmethod
    def add_condiments(self):
        pass

    def boil_water(self):
        print("boil water")

    def pour_in_cup(self):
        print("pour in cup")
