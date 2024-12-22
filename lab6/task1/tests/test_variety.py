import sys
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(CURRENT_DIR, '..', '..')
sys.path.insert(0, SRC_DIR)

import unittest

from lab6.task1.src.variety import variety

class TestVariety(unittest.TestCase):

    def test_should_check_the_possibility_of_solving_1st_set_of_operations(self):
        # given
        n = 8
        array = ['A', '2', 'A', '5', 'A', '3', '?', '2', '?', '4', 'A', '2', 'D', '2', '?', '2']
        expected_result = ['Y\n', 'N\n', 'N\n']

        # when
        result = variety(array)

        # then
        self.assertEqual(result, expected_result)

    def test_should_check_the_possibility_of_solving_2nd_set_of_operations(self):
        # given
        n = 8
        array = ['A', '2', 'A', '5', 'A', '3', '?', '8', '?', '3', 'A', '2', 'D', '2', '?', '2']
        expected_result = ['N\n', 'Y\n', 'N\n']

        # when
        result = variety(array)

        # then
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()