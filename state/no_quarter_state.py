'''
Created on 2017/03/18

@author: yu-suke
'''
from state.abc_state import State


class NoQuarterState(State):
    '''
    NoQuarterState class
    '''

    def __init__(self, gum_ball_machine):
        '''
        Constructor
        '''
        super().__init__(gum_ball_machine)

    def insert_quarter(self):
        print("put in 25 cents")
        self._gum_ball_machine.set_state(
            self._gum_ball_machine.get_has_quarter_state())

    def eject_quarter(self):
        print("hasn't put in 25 cents")

    def turn_crank(self):
        print("You turn the crank, but you didn't put in 25 cents")

    def dispense(self):
        print("First you nead to make payment")
