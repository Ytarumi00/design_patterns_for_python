'''
Created on 2016/08/10

@author: yu-suke
'''
from command.command_package.command import Command


class MacroCommand(Command):
    '''
    MacroCommand class
    '''

    def __init__(self, commands):
        self.commands = commands

    def execute(self):
        for command in self.commands:
            command.execute()

    def undo(self):
        for command in self.commands:
            command.undo()
