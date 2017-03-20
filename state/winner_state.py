'''
Created on 2017/03/19

@author: yu-suke
'''
from state.abc_state import State


class WinnerState(State):
    '''
    WinnerState class
    '''

    def __init__(self, gum_ball_machine):
        '''
        Constructor
        '''
        self._gum_ball_machine = gum_ball_machine

    def insert_quarter(self):
        print("Please wait ALready have a gumball on hand")

    def eject_quarter(self):
        print("Sorry. I already turned the crank")

    def turn_crank(self):
        print("You cann't get another gmuball even after twice doing it")

    def dispense(self):
        print("It is hit. You get 2 gum balls at 25 cents.")
        self._gum_ball_machine.release_ball()
        if self._gum_ball_machine.count == 0:
            self._gum_ball_machine.set_state(
                self._gum_ball_machine.get_sold_out_state())
        else:
            self._gum_ball_machine.release_ball()
            if self._gum_ball_machine.count > 0:
                self._gum_ball_machine.set_state(
                    self._gum_ball_machine.get_no_quarter_state())
            else:
                print("Gum ball are gone.")
                self._gum_ball_machine.set_state(
                    self._gum_ball_machine.get_sold_out_state())
