'''
Created on 2016/08/05

@author: yu-suke
'''
from command.vender_class.garagedoor import GarageDoor
from command.command_package.command import Command

class GarageDoorDownCommand(Command):

    def __init__(self, garagedoor: GarageDoor):
        self.garagedoor =garagedoor
    
    def execute(self):
        self.garagedoor.down()