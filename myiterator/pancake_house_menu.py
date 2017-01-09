'''
Created on 2017/01/06

@author: yu-suke
'''
from myiterator.menu_item import MenuItem
from myiterator.menu import Menu


class PancakeHouseMenu(Menu):
    '''
    PancakeHouseMenu class
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.menu_items = []
        self.addItem("K&B pancake breakfast",
                     "pancake with scrambled egg and a toast", True, 2.99)
        self.addItem("basic pancake breakfast",
                     "pancake with fried egg and a sausage", True, 3.49)

    def addItem(self, name: str, description: str,
                vegetarian: bool, price: float):
        menu_item = MenuItem(name, description, vegetarian, price)
        self.menu_items.append(menu_item)

    # def get_menu_items(self):
    #    return self.menu_items

    def create_iterator(self):
        return self.menu_items.__iter__()

if __name__ == "__main__":
    pancake_house_menu = PancakeHouseMenu()
    pancake_house_menu_iterator = pancake_house_menu.create_iterator()
    for menu in pancake_house_menu_iterator:
        print("name :{}\n{}\nvegetarian:{}\nprice:{}".format(
            menu.get_name(), menu.get_description(), menu.get_vegetarian(),
            menu.get_price()))
