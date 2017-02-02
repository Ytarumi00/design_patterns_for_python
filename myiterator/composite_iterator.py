'''
Created on 2017/01/30

@author: yu-suke
'''
from _collections_abc import Iterator
from builtins import isinstance
from myiterator.menu_item import MenuItem


class CompositeIterator(Iterator):
    '''
    CompositeIterator class
    '''

    def __init__(self, iterator: Iterator):
        '''
        Constructor
        '''
        self.stack = list()
        self.stack.append(iterator)
        self.generator = self.generate()

    def __next__(self):
        return self.generator.__next__()

    def generate(self):
        from myiterator.menu import Menu
        while(True):
            if(len(self.stack) == 0):
                raise StopIteration
            try:
                iterator = self.stack.pop(0)
                for component in iterator:
                    if(isinstance(component, Menu)):
                        self.stack.append(iter(component.menu_components))
                    yield component

            except Exception as e:
                print(e)

if __name__ == "__main__":
    from myiterator.menu import Menu

    pancake_house_menu = Menu("Pancake house menu", "breakfirst")
    diner_menu = Menu("diner menu", "lunch")
    cafe_menu = Menu("cafe menu", "dinner")
    dessert_nenu = Menu("dessert_menu", "dessert")

    all_menus = Menu("all menus", "menu with all integrated")

    all_menus.add(pancake_house_menu)
    all_menus.add(diner_menu)
    all_menus.add(cafe_menu)

    pancake_house_menu.add(MenuItem("K&B pancake breakfast",
                                    "pancake with scrambled egg and a toast",
                                    True, 2.99))
    pancake_house_menu.add(MenuItem("basic pancake breakfast",
                                    "pancake with fried egg and a sausage",
                                    True, 3.49))

    iterator = all_menus.create_iterator()
    for i in iterator:
        print(i.get_name())
