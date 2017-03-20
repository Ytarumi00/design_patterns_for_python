'''
Created on 2017/03/20

@author: yu-suke
'''
import unittest
from state.no_quarter_state import NoQuarterState
from state.gum_ball_machine import GumballMachine
from state.has_quarter_state import HasQuarterState
from state.sold_out_state import SoldOutState
from state.sold_state import SoldState
from state.winner_state import WinnerState


class Test(unittest.TestCase):

    def setUp(self):
        self.gum_ball_machine = GumballMachine(50)
        self.gum_ball_machine.insert_quarter()

    def tearDown(self):
        pass

    def test_insert_quarter(self):
        self.gum_ball_machine.insert_quarter()
        self.assertIsInstance(self.gum_ball_machine._state, HasQuarterState)

    def test_eject_quarter(self):
        self.gum_ball_machine.eject_quarter()
        self.assertIsInstance(self.gum_ball_machine._state, NoQuarterState)

    def test_turn_clank_to_sold(self):
        self.gum_ball_machine._state.is_winner = False
        self.gum_ball_machine._state.turn_crank()
        self.assertIsInstance(
            self.gum_ball_machine._state, SoldState)

    def test_turn_clank_to_winner(self):
        self.gum_ball_machine._state.is_winner = True
        self.gum_ball_machine._state.turn_crank()
        self.assertIsInstance(
            self.gum_ball_machine._state, WinnerState)

    def test_dispense(self):
        self.gum_ball_machine._state.dispense()
        self.assertIsInstance(self.gum_ball_machine._state, HasQuarterState)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
