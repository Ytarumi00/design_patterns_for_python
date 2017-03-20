'''
Created on 2017/03/18

@author: yu-suke
'''
from state.sold_out_state import SoldOutState
from state.no_quarter_state import NoQuarterState
from state.has_quarter_state import HasQuarterState
from state.sold_state import SoldState
from state.winner_state import WinnerState


class GumballMachine(object):
    '''
    Gumball machine class
    '''

    def __init__(self, num_gumballs):
        '''
        Constructor
        '''
        self._sold_out_sate = SoldOutState(self)
        self._no_quarter_state = NoQuarterState(self)
        self._has_quarter_state = HasQuarterState(self)
        self._sold_state = SoldState(self)
        self._winner_state = WinnerState(self)
        self._count = num_gumballs
        if self._count > 0:
            self._state = self._no_quarter_state
        else:
            self._state = self._sold_out_sate

    def insert_quarter(self):
        self._state.insert_quarter()

    def eject_quarter(self):
        self._state.eject_quarter()

    def turn_crank(self):
        self._state.turn_crank()
        self._state.dispense()

    def set_state(self, state):
        self._state = state

    def release_ball(self):
        print("Gum ball rolls out of the slot...")
        if self._count > 0:
            self._count -= 1

    def get_sold_out_state(self):
        return self._sold_out_sate

    def get_no_quarter_state(self):
        return self._no_quarter_state

    def get_has_quarter_state(self):
        return self._has_quarter_state

    def get_sold_state(self):
        return self._sold_state

    def get_winner_state(self):
        return self._winner_state

    def refill(self, count):
        if count > 0:
            self._count += count
            self._state = self.get_no_quarter_state()
        else:
            raise UserWarning("count is upper than 0")

    @property
    def count(self):
        return self._count
