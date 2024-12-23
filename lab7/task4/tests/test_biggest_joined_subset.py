import sys
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(CURRENT_DIR, '..', '..')
sys.path.insert(0, SRC_DIR)

import unittest

from lab7.task4.src.biggest_joined_subset import biggest_joined_subset

class TestBiggestJoinedSubset(unittest.TestCase):

    def test_should_check_the_possibility_of_calculating_the_length_of_two_1st_sets_joined_subset(self):
        # given
        array_1 = ['2', '7', '8', '3']
        array_2 = ['5', '2', '8', '7']
        expected_result = 2
        
        # when
        result = biggest_joined_subset(array_1, array_2)

        # then
        self.assertEqual(result, expected_result)

    def test_should_check_the_possibility_of_calculating_the_length_of_two_2nd_sets_joined_subset(self):
        # given
        array_1 = ["7"]
        array_2 = ["1", "2", "3", "4"]
        expected_result = 0

        # when
        result = biggest_joined_subset(array_1, array_2)

        # then
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()