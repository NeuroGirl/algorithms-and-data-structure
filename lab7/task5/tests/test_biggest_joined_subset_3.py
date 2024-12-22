import sys
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(CURRENT_DIR, '..', '..')
sys.path.insert(0, SRC_DIR)

import unittest

from lab7.task5.src.biggest_joined_subset_3 import biggest_joined_subset_3

class TestBiggestJoinedSubset3(unittest.TestCase):

    def test_should_check_the_possibility_of_calculating_the_length_of_three_1st_sets_joined_subset(self):
        # given
        n = 3
        array_1 = ['1', '2', '3']
        m = 3
        array_2 = ['2', '1', '3']
        k = 3
        array_3 = ['1', '3', '5']
        expected_result = 2

        # when
        result = biggest_joined_subset_3(array_1, array_2, array_3)

        # then
        self.assertEqual(result, expected_result)

    def test_should_check_the_possibility_of_calculating_the_length_of_three_2nd_sets_joined_subset(self):
        # given
        n = 5
        array_1 = ['8', '3', '2', '1', '7']
        m = 7
        array_2 = ['8', '2', '1', '3', '8', '10', '7']
        k = 6
        array_3 = ['6', '8', '3', '1', '4', '7']
        expected_result = 3

        # when
        result = biggest_joined_subset_3(array_1, array_2, array_3)

        # then
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()