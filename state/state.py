'''
Created on 2017/03/12

@author: yu-suke
'''
from abc import ABCMeta


class State(metaclass=ABCMeta):
    '''
    Abstract class
    '''

    def __init__(self):
        '''
        Constructor
        '''

    def insertQuarter(self):
        pass

    def ejectQuarter(self):
        pass

    def turnCrank(self):
        pass

    def dispense(self):
        pass
