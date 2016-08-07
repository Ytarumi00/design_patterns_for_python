from command.command_package.command import Command

class SimpleRemoteControl:
  
  def __init__(self):
    pass
  
  def setCommand(self, command :Command):
    self.slot = command
    
  def buttonWasPressed(self):
    self.slot.execute()
    