'''
Created on 2017/01/30

@author: yu-suke
'''
from _collections_abc import Iterator


class NullIterator(Iterator):
    '''
    NullIterator class
    '''

    def __init__(self):
        '''
        Constructor
        '''
        pass

    def __next__(self):
        print("now null iterator")
        return None
