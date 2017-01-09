'''
Created on 2017/01/08

@author: yu-suke
'''
from myiterator.iterator import Iterator


class DinerMenuIterator(Iterator):
    '''
    DinerMenuIterator class
    '''

    def __init__(self, items: dict):
        '''
        Constructor
        '''
        self.items = items
        self.position = 0

    def next(self):
        item = self.items.get(str(self.position))
        self.position += 1
        return item

    def has_next(self) -> bool:
        if(self.position >= len(self.items) or
           self.items.get(str(self.position)) == None):
            return False
        else:
            return True
