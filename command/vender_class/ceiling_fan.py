'''
Created on 2016/08/09

@author: yu-suke
'''


class CeilingFan:
    '''
    Vender class for ceiling fan
    '''

    HIGH = 3
    MEDIUM = 2
    LOW = 1
    OFF = 0

    def __init__(self, location):
        '''
        Constructor
        '''
        self.location = location
        self.speed = CeilingFan.OFF

    def high(self):
        self.speed = CeilingFan.HIGH

    def medium(self):
        self.speed = CeilingFan.MEDIUM

    def low(self):
        self.speed = CeilingFan.LOW

    def off(self):
        self.speed = CeilingFan.OFF

    def getSpeed(self):
        return self.speed

    def getStatus(self):
        return "Fan's strength is {} ".format(self.getSpeed())
