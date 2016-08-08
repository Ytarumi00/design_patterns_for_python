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
    
    noCommand = NoCommand()
    self.undoCommand =  noCommand
    
    for slot in range(7):
      self.onCommand[slot] = noCommand
      self.offCommand[slot] = noCommand
          
  def setCommand(self, slot, onCommand, offCommand):
    self.onCommand[slot] = onCommand
    self.offCommand[slot] = offCommand
      
  def onButtonWasPushed(self, slot):
    self.onCommand[slot].execute()
    self.undoCommand = self.onCommand[slot]
      
  def offButtonWasPushed(self, slot):
    self.offCommand[slot].execute()
    self.undoCommand = self.offCommand[slot]
      
  def undoButtonWasPushed(self): 
    self.undoCommand.undo()
    
  def __repr__(self):
    rstr=""
    for i, v in enumerate(self.onCommand):
      rstr += "[slot {0}] {1}   {2}\n".format(i, self.onCommand[i], self.offCommand[i])
      
    rstr += "[undo] {}\n".format(self.undoCommand)
    return rstr