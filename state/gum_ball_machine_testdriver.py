'''
Created on 2017/03/19

@author: yu-suke
'''
from state.gum_ball_machine import GumballMachine


if __name__ == '__main__':
    gum_ball_machine = GumballMachine(20)

    for i in range(20):
        gum_ball_machine.insert_quarter()
        gum_ball_machine.turn_crank()
