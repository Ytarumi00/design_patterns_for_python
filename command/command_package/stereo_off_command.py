'''
Created on 2016/08/05

@author: yu-suke
'''
from command.vender_class.stereo import Stereo
from command.command_package.command import Command

class StereoOffCommand(Command):

    def __init__(self, stereo: Stereo):
        self.stereo = stereo
        
    def execute(self):
        self.stereo.off()
        
        