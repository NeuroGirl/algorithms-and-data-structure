import sys
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(CURRENT_DIR, '..', '..')
sys.path.insert(0, SRC_DIR)

import unittest

from lab7.task1.src.money_exchange import min_coins

class TestMoneyExchange(unittest.TestCase):

    def test_should_check_the_possibility_of_solving_1st_coin_exchange_puzzle(self):
        # given
        n = 34
        array = ['1', '3', '4']
        expected_result = 9

        # when
        result = min_coins(n, array)

        # then
        self.assertEqual(result, expected_result)

    def test_should_check_the_possibility_of_solving_2nd_coin_exchange_puzzle(self):
        # given
        n = 2
        array = ['1', '3', '4']
        expected_result = 2

        # when
        result = min_coins(n, array)

        # then
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()