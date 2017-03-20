
from command.invoker.remote_control import RemoteControl
from command.vender_class.light import Light
from command.command_package.light_on_command import LightOnCommand
from command.command_package.light_off_command import LightOffComand
from command.vender_class.ceiling_fan import CeilingFan
from command.command_package.ceiling_fan_medium_command import CeilingFanMediumCommand
from command.command_package.ceiling_fan_high_command import CeilingFanHighCommand
from command.command_package.ciling_fan_off_command import CeilingFanOffCommand
from command.vender_class.stereo import Stereo
from command.command_package.stereo_on_With_CD_Command import StereoOnWithCDCommand
from command.command_package.stereo_off_command import StereoOffCommand
from command.command_package.macro_command import MacroCommand


if __name__ == '__main__':

    light = Light("LIving Room")
    stereo = Stereo("Living Room")
    ceilingFan = CeilingFan("Living Room")

    lightOn = LightOnCommand(light)
    lightOff = LightOffComand(light)

    stereoOn = StereoOnWithCDCommand(stereo)
    stereoOff = StereoOffCommand(stereo)

    ceilingFanOn = CeilingFanMediumCommand(ceilingFan)
    ceilingFanOff = CeilingFanOffCommand(ceilingFan)

    mySetOn = {lightOn, stereoOn, ceilingFanOn}
    mySetOff = {lightOff, stereoOff, ceilingFanOff}

    MyMacroOn = MacroCommand(mySetOn)
    MyMacroOff = MacroCommand(mySetOff)

    remoteControl = RemoteControl()
    remoteControl.setCommand(0, MyMacroOn, MyMacroOff)

    print(repr(remoteControl))
    print("\npushed on button.\n")
    remoteControl.onButtonWasPushed(0)
    print("\npushed off button.\n")
    remoteControl.offButtonWasPushed(0)
    print("\npushed undo button.\n")
    remoteControl.undoButtonWasPushed()