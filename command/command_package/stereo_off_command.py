'''
Created on 2016/08/05

@author: yu-suke
'''
from command.vender_class.stereo import Stereo
from command.command_package.command import Command

class StrereoOffCommand(Command):

    def __init__(self, stereo: Stereo):
        self.Stereo = stereo
        
    def execute(self):
        self.stereo.off()
        
        