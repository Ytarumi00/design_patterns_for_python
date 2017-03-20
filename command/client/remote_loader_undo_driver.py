'''
Created on 2016/08/09

@author: yu-suke
'''
from command.invoker.remote_control import RemoteControl
from command.vender_class.light import Light
from command.command_package.light_on_command import LightOnCommand
from command.command_package.light_off_command import LightOffComand
from command.vender_class.ceiling_fan import CeilingFan
from command.command_package.ceiling_fan_medium_command import CeilingFanMediumCommand
from command.command_package.ceiling_fan_high_command import CeilingFanHighCommand
from command.command_package.ciling_fan_off_command import CeilingFanOffCommand

if __name__ == '__main__':
    remoteControl = RemoteControl()

    livingRoomLight = Light("Living Room")
    ceilingFan = CeilingFan("Living Room")

    livingRoomLightOn = LightOnCommand(livingRoomLight)
    livingRoomLightOff = LightOffComand(livingRoomLight)

    ceilingFanMedium = CeilingFanMediumCommand(ceilingFan)
    ceilingFanHigh = CeilingFanHighCommand(ceilingFan)
    ceilingFanOff = CeilingFanOffCommand(ceilingFan)

    remoteControl.setCommand(0, livingRoomLightOn, livingRoomLightOff)
    remoteControl.setCommand(1, ceilingFanHigh, ceilingFanOff)
    remoteControl.setCommand(2, ceilingFanMedium, ceilingFanOff)

    remoteControl.onButtonWasPushed(0)
    remoteControl.offButtonWasPushed(0)
    print(repr(remoteControl))
    remoteControl.undoButtonWasPushed()
    remoteControl.offButtonWasPushed(0)
    remoteControl.onButtonWasPushed(0)
    print(repr(remoteControl))
    remoteControl.undoButtonWasPushed()

    remoteControl.onButtonWasPushed(2)
    remoteControl.offButtonWasPushed(2)
    print(repr(remoteControl))
    remoteControl.undoButtonWasPushed()

    remoteControl.onButtonWasPushed(1)
    print(repr(remoteControl))
    remoteControl.undoButtonWasPushed()
