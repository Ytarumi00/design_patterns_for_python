'''
Created on 2017/01/08

@author: yu-suke
'''
from abc import ABCMeta, abstractmethod


class Iterator(metaclass=ABCMeta):
    '''
    Iterator class
    '''

    def __init__(self):
        '''
        Constructor
        '''

    @abstractmethod
    def has_next(self) -> bool:
        pass

    @abstractmethod
    def next(self):
        pass
