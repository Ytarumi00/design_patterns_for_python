'''
Created on 2016/08/09

@author: yu-suke
'''
from command.command_package.command import Command
from command.vender_class.ceiling_fan import CeilingFan


class CeilingFanLowCommadn(Command):
    '''
    concrete command class for ceiling fan status changed high
    '''

    def __init__(self, ceilingFan):
        '''
        Constructor
        '''
        self.ceilingFan = ceilingFan

    def execute(self):
        self.prevSpeed = self.ceilingFan.getSpeed()
        self.ceilingFan.low()

    def undo(self):
        if(self.prevSpeed == CeilingFan.__HIGH):
            self.ceilingFan.high()
        elif(self.prevSpeed == CeilingFan.__MEDIUM):
            self.ceilingFan.medium()
        elif(self.prevSpeed == CeilingFan.__LOW):
            self.ceilingFan.low()
        elif(self.prevSpeed == CeilingFan.__OFF):
            self.ceilingFan.off()
