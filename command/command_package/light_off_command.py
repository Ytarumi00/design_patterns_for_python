'''
Created on 2016/08/05

@author: yu-suke
'''
from command.command_package.command import Command

class LightOffComand(Command):

  def __init__(self, light):
    self.light = light
        
  def execute(self):
    self.light.off()
      
  def undo(self):
    self.light.on()
    
