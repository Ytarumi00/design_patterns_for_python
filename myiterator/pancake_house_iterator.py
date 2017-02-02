'''
Created on 2017/01/09

@author: yu-suke
'''
from myiterator.iterator import Iterator


class PancakeHouseIterator(Iterator):
    '''
    PancakeHouseIterator class
    '''

    def __init__(self, items: list):
        '''
        Constructor
        '''
        self.items = items
        self.position = 0

    def next(self):
        item = self.items[self.position]
        self.position += 1
        return item

    def has_next(self) -> bool:
        if(self.position >= len(self.items)):
            return False
        else:
            return True
