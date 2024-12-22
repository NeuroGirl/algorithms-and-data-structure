import sys
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(CURRENT_DIR, '..', '..')
sys.path.insert(0, SRC_DIR)

import unittest

from task6.src.fibonachi import fibonachi

class TestFibonachi(unittest.TestCase):

    def test_should_check_the_possibility_of_searching_fibonachi_numbers_in_1st_array(self):
        # given
        array = ['1', '2', '3', '4', '5', '6', '7', '8']
        expected_result = ['Yes\n', 'Yes\n', 'Yes\n', 'No\n', 'Yes\n', 'No\n', 'No\n', 'Yes\n']

        # when
        result = fibonachi(array)

        # then
        self.assertEqual(result, expected_result)

    def test_should_check_the_possibility_of_searching_fibonachi_numbers_in_2nd_array(self):
        # given
        array = ['1', '2', '3', '4', '5', '6', '7', '8', '13', '0']
        expected_result = ['Yes\n', 'Yes\n', 'Yes\n', 'No\n', 'Yes\n', 'No\n', 'No\n', 'Yes\n', 'Yes\n', 'Yes\n']

        # when
        result = fibonachi(array)

        # then
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()