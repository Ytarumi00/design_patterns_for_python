'''
Created on 2017/03/20

@author: yu-suke
'''
import unittest
from state.gum_ball_machine import GumballMachine
from state.sold_state import SoldState
from state.no_quarter_state import NoQuarterState
from state.sold_out_state import SoldOutState


class Test(unittest.TestCase):

    def setUp(self):
        self.gum_ball_machine = GumballMachine(50)
        self.gum_ball_machine.set_state(self.gum_ball_machine.get_sold_state())

    def tearDown(self):
        pass

    def test_insert_quarter(self):
        self.gum_ball_machine.insert_quarter()
        self.assertIsInstance(self.gum_ball_machine._state, SoldState)

    def test_eject_quarter(self):
        self.gum_ball_machine.eject_quarter()
        self.assertIsInstance(self.gum_ball_machine._state, SoldState)

    def test_turn_clank1(self):
        self.gum_ball_machine._state.turn_crank()
        self.assertIsInstance(
            self.gum_ball_machine._state, SoldState)

    def test_dispense_to_no_quarter(self):
        self.gum_ball_machine._state.dispense()
        self.assertIsInstance(self.gum_ball_machine._state, NoQuarterState)

    def test_dispense_to_sold_out(self):
        self.gum_ball_machine._count = 1
        self.gum_ball_machine._state.dispense()
        self.assertIsInstance(self.gum_ball_machine._state, SoldOutState)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
