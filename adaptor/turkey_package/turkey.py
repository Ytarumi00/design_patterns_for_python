'''
Created on 2016/08/13

@author: yu-suke
'''
from abc import ABC, ABCMeta, abstractmethod


class Turkey(metaclass=ABCMeta):
    '''
    ABC class for turkey
    '''
    
    @abstractmethod
    def gobble(self):
        pass
    
    @abstractmethod
    def fly(self):
        pass
    