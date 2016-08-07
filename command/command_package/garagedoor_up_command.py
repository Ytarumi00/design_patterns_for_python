from command.command_package.command import Command
from command.vender_class.garagedoor import GarageDoor

class GarageDoorUpCommand(Command):
  
  def __init__(self, garagedoor: GarageDoor):
    self.garagedoor = garagedoor
    
  def execute(self):
    self.garagedoor.up()
