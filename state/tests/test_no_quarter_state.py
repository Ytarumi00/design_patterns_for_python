'''
Created on 2017/03/20

@author: yu-suke
'''
import unittest
from state.no_quarter_state import NoQuarterState
from state.gum_ball_machine import GumballMachine
from state.has_quarter_state import HasQuarterState


class Test(unittest.TestCase):

    def setUp(self):
        self.gum_ball_machine = GumballMachine(50)

    def tearDown(self):
        pass

    def test_insert_quarter(self):
        self.gum_ball_machine.insert_quarter()
        self.assertIsInstance(self.gum_ball_machine._state, HasQuarterState)

    def test_eject_quarter(self):
        self.gum_ball_machine.eject_quarter()
        self.assertIsInstance(self.gum_ball_machine._state, NoQuarterState)

    def test_turn_clank(self):
        self.gum_ball_machine.turn_crank()
        self.assertIsInstance(self.gum_ball_machine._state, NoQuarterState)

    def test_dispense(self):
        self.gum_ball_machine._state.dispense()
        self.assertIsInstance(self.gum_ball_machine._state, NoQuarterState)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
