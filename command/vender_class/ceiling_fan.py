'''
Created on 2016/08/09

@author: yu-suke
'''


class CeilingFan:
    '''
    Vender class for ceiling fan
    '''

    __HIGH = 3
    __MEDIUM = 2
    __LOW = 1
    __OFF = 0

    def __init__(self, location):
        '''
        Constructor
        '''
        self.location = location
        self.speed = CeilingFan.__OFF

    def high(self):
        self.speed = CeilingFan.__HIGH

    def medium(self):
        self.speed = CeilingFan.__MEDIUM

    def low(self):
        self.speed = CeilingFan.__LOW

    def off(self):
        self.speed = CeilingFan.__OFF

    def getSpeed(self):
        return self.speed
