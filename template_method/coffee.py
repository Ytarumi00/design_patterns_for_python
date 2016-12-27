'''
Created on 2016/12/27

@author: yu-suke
'''
from template_method.caffeine_beverage import CaffeineBeverage


class Coffee(CaffeineBeverage):
    '''
    Coffee class
    '''

    def brew(self):
        print("brew a cup of coffee")

    def add_condiments(self):
        print("add sugar and milk")

if __name__ == "__main__":
    coffee = Coffee()
    coffee.prepare_recipe()
