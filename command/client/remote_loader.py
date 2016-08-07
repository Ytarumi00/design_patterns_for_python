'''
Created on 2016/08/07

@author: yu-suke
'''
from command.invoker.remote_control import RemoteControl
from command.vender_class.light import Light
from command.vender_class.garagedoor import GarageDoor
from command.vender_class.stereo import Stereo
from command.command_package.light_on_command import LightOnCommand
from command.command_package.light_off_command import LightOffComand
from command.command_package.garagedoor_up_command import GarageDoorUpCommand
from command.command_package.garagedoor_down_command import GarageDoorDownCommand
from command.command_package.stereo_on_With_CD_Command import StereoOnWithCDCommand
from command.command_package.stereo_off_command import StereoOffCommand

if __name__ == '__main__':
    remote_control = RemoteControl()
    livingRoomLight = Light("Living Room")
    kitchenLight = Light("Kitchen")
    garageDoor = GarageDoor()
    stereo = Stereo("Living Room")
    
    
    livingRoomLightOn = LightOnCommand(livingRoomLight)
    livingRoomLightOff = LightOffComand(livingRoomLight)
    kitchenLightOn = LightOnCommand(kitchenLight)
    kitchenLightOff = LightOffComand(kitchenLight)
    
    garageDoorUp = GarageDoorUpCommand(garageDoor)
    garageDoorDown = GarageDoorDownCommand(garageDoor)
    
    stereoOnWithCO = StereoOnWithCDCommand(stereo)
    stereoOff = StereoOffCommand(stereo)
    
    remote_control.setCommand(0, livingRoomLightOn, livingRoomLightOff)
    remote_control.setCommand(1, kitchenLightOn, kitchenLightOff)
    remote_control.setCommand(2, stereoOnWithCO, stereoOff)
    remote_control.setCommand(3, garageDoorUp, garageDoorDown)
    
    remote_control.onButtonWasPushed(0)
    remote_control.offButtonWasPushed(0)
    remote_control.onButtonWasPushed(1)
    remote_control.offButtonWasPushed(1)
    remote_control.onButtonWasPushed(2)
    remote_control.offButtonWasPushed(2)
    remote_control.onButtonWasPushed(3)
    remote_control.offButtonWasPushed(3)
    remote_control.onButtonWasPushed(4)
    remote_control.offButtonWasPushed(4)