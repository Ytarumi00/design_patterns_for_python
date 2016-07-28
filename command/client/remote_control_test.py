
'''
Client for SimpleRemoteControl test
'''
from command.invoker.simple_remote_control import SimpleRemoteControl
from command.vender_class.light import Light
from command.commnad_package.light_on_command import LightOnCommand

if __name__ == "__main__":
  remote = SimpleRemoteControl()
  light = Light()
  light_on = LightOnCommand(light)
  
  remote.setCommand(light_on)
  remote.buttonWasPressed()
  

  