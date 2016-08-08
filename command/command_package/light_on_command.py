from command.command_package.command import Command
from command.vender_class.light import Light

class LightOnCommand(Command):
  
  def __init__(self, light :Light):
    self.light = light
    
  def execute(self):
    self.light.on()
    
  def undo(self):
    self.light.off()


