'''
Created on 2016/12/27

@author: yu-suke
'''
from template_method.caffeine_beverage import CaffeineBeverage


class Tea(CaffeineBeverage):
    '''
    Tea class
    '''

    def brew(self):
        print("brew a cup of tea")

    def add_condiments(self):
        print("add lemon")

if __name__ == "__main__":
    tea = Tea()
    tea.prepare_recipe()
