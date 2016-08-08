'''
Created on 2016/08/09

@author: yu-suke
'''
from command.invoker.remote_control import RemoteControl
from command.vender_class.light import Light
from command.command_package.light_on_command import LightOnCommand
from command.command_package.light_off_command import LightOffComand

if __name__ == '__main__':
  remoteControl = RemoteControl()
  
  livingRoomLight = Light("Living Room")
  
  livingRoomLightOn = LightOnCommand(livingRoomLight)
  livingRoomLightOff = LightOffComand(livingRoomLight)
  
  remoteControl.setCommand(0, livingRoomLightOn, livingRoomLightOff)
  
  remoteControl.onButtonWasPushed(0)
  remoteControl.offButtonWasPushed(0)
  print(repr(remoteControl))
  remoteControl.undoButtonWasPushed()
  remoteControl.offButtonWasPushed(0)
  remoteControl.onButtonWasPushed(0)
  print(repr(remoteControl))
  remoteControl.undoButtonWasPushed()