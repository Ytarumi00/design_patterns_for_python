'''
Created on 2017/01/08

@author: yu-suke
'''
#from myiterator.iterator import Iterator
from _collections_abc import Iterator


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

    def __next__(self):
        if(self.position >= len(self.items) or
           self.items.get(str(self.position)) == None):
            raise StopIteration()
        item = self.items.get(str(self.position))
        self.position += 1
        return item
