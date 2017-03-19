'''
Created on 2017/03/18

@author: yu-suke
'''
from state.abc_state import State


class HasQuarterState(State):
    '''
    HasQuarterState class
    '''

    def __init__(self, gum_ball_machine):
        '''
        Constructor
        '''
        super().__init__(gum_ball_machine)

    def insert_quarter(self):
        print("You cann't put in another 25 cents again")

    def eject_quarter(self):
        print("I return 25 cents")
        self._gum_ball_machine.set_state(
            self._gum_ball_machine.get_no_quarter_state())

    def turn_crank(self):
        print("Turned the crank")
        self._gum_ball_machine.set_state(
            self._gum_ball_machine.get_sold_state())

    def dispense(self):
        print("There is no gum ball to sell")
