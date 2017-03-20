'''
Created on 2017/03/12

@author: yu-suke
'''
from abc import ABCMeta, abstractmethod


class State(metaclass=ABCMeta):
    '''
    Abstract class
    '''

    def __init__(self, gum_ball_machine):
        '''
        Constructor
        '''
        self._gum_ball_machine = gum_ball_machine

    @abstractmethod
    def insert_quarter(self):
        pass

    @abstractmethod
    def eject_quarter(self):
        pass

    @abstractmethod
    def turn_crank(self):
        pass

    @abstractmethod
    def dispense(self):
        pass
