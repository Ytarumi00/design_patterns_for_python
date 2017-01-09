'''
Created on 2017/01/09

@author: yu-suke
'''
from abc import ABCMeta, abstractmethod


class Menu(metaclass=ABCMeta):
    '''
    Menu class
    '''

    def __init__(self):
        '''
        Constructor
        '''

    @abstractmethod
    def create_iterator(self):
        pass
