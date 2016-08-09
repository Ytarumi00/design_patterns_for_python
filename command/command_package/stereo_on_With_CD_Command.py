'''
Created on 2016/08/07

@author: yu-suke
'''
from command.vender_class.stereo import Stereo
from command.command_package.command import Command


class StereoOnWithCDCommand(Command):

    def __init__(self, stereo: Stereo):
        self.stereo = stereo

    def execute(self):
        self.stereo.on()
        self.stereo.setCD()
        self.stereo.setVolume(11)

    def undo(self):
        self.stereo.off()
