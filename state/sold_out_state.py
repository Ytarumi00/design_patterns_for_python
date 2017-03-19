'''
Created on 2017/03/19

@author: yu-suke
'''
from state.abc_state import State


class SoldOutState(State):
    '''
    SoldOutState class
    '''

    def __init__(self, gum_ball_machine):
        '''
        Constructor
        '''
        super().__init__(gum_ball_machine)

    def insert_quarter(self):
        print("You cann't put in 25 cents. This machine is sold out")

    def eject_quarter(self):
        print("Cann't be refunded. I have not put in 25 cents yet")

    def turn_crank(self):
        print("Turned the crank, but there is no gumball")

    def dispense(self):
        print("There is no gumball to sell")
