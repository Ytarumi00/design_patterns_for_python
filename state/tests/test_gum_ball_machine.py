'''
Created on 2017/03/20

@author: yu-suke
'''
import unittest
from state.gum_ball_machine import GumballMachine
from state.sold_out_state import SoldOutState


class Test(unittest.TestCase):

    def setUp(self):
        self.gum_ball_machine = GumballMachine(1)

    def tearDown(self):
        del(self.gum_ball_machine)

    def test_gum_ball_sell(self):
        self.assertEqual(1, self.gum_ball_machine.count)
        self.gum_ball_machine.insert_quarter()
        self.gum_ball_machine.turn_crank()
        self.assertIsInstance(self.gum_ball_machine._state, SoldOutState)
        self.assertEqual(0, self.gum_ball_machine.count)

    def test_refill(self):
        self.gum_ball_machine.refill(10)
        self.assertEqual(self.gum_ball_machine.count, 11)
        with self.assertRaises(UserWarning):
            self.gum_ball_machine.refill(0)
        with self.assertRaises(UserWarning):
            self.gum_ball_machine.refill(-1)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
