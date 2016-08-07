'''
Created on 2016/08/05

@author: yu-suke
'''
from command.command_package.nocommand import NoCommand
from command.command_package.command import Command

class RemoteControl:

    def __init__(self):
        self.onCommand = {}
        self.offCommand = {}
        
        for slot in range(7):
            self.onCommand[slot] = NoCommand()
            self.offCommand[slot] = NoCommand()
            
    def setCommand(self, slot, onCommand, offCommand):
        self.onCommand[slot] = onCommand
        self.offCommand[slot] = offCommand
        
    def onButtonWasPushed(self, slot):
        self.onCommand[slot].execute()
        
    def offButtonWasPushed(self, slot):
        self.offCommand[slot].execute()
        