
'''
Client for SimpleRemoteControl test
'''
from command.invoker.simple_remote_control import SimpleRemoteControl
from command.vender_class.light import Light
from command.command_package.light_on_command import LightOnCommand
from command.vender_class.garagedoor import GarageDoor
from command.command_package.garagedoor_up_command import GarageDoorOpenCommand

if __name__ == "__main__":
    remote = SimpleRemoteControl()
    light = Light()
    garagedoor = GarageDoor()
    light_on = LightOnCommand(light)
    garagedoor_open = GarageDoorOpenCommand(garagedoor)

    remote.setCommand(light_on)
    remote.buttonWasPressed()
    remote.setCommand(garagedoor_open)
    remote.buttonWasPressed()
