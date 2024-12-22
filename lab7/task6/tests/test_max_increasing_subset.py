import sys
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(CURRENT_DIR, '..', '..')
sys.path.insert(0, SRC_DIR)

import unittest

from lab7.task6.src.max_increasing_subset import max_increasing_subsequence

class TestMaxIncreasingSubset(unittest.TestCase):

    def test_should_check_the_possibility_of_finding_max_increasing_subset_in_1st_array(self):
        # given
        array = ['3', '29', '5', '5', '28', '6']
        expected_result = ['3\n', '3 ', '5 ', '28 ']
        # when
        result = max_increasing_subsequence(array)

        # then
        self.assertEqual(result, expected_result)

    def test_should_check_the_possibility_of_finding_max_increasing_subset_in_2nd_array(self):
        # given
        array = ['3', '4', '5', '8', '1', '13', '0', '9']
        expected_result = ['5\n', '3 ', '4 ', '5 ', '8 ', '13 ']
        # when
        result = max_increasing_subsequence(array)

        # then
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()