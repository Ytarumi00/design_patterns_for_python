'''
Created on 2017/03/19

@author: yu-suke
'''
from state.gum_ball_machine import GumballMachine


if __name__ == '__main__':
    gum_ball_machine = GumballMachine(2)

    print(gum_ball_machine)

    gum_ball_machine.insert_quarter()
    gum_ball_machine.turn_crank()
    print()

    gum_ball_machine.insert_quarter()
    gum_ball_machine.eject_quarter()
    gum_ball_machine.turn_crank()
    print()

    gum_ball_machine.insert_quarter()
    gum_ball_machine.turn_crank()
    gum_ball_machine.turn_crank()
    print()

    gum_ball_machine.insert_quarter()
    gum_ball_machine.insert_quarter()
    gum_ball_machine.turn_crank()
    print()

    gum_ball_machine.insert_quarter()
    gum_ball_machine.insert_quarter()
    gum_ball_machine.turn_crank()
