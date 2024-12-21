import sys
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(CURRENT_DIR, '..', '..')
sys.path.insert(0, SRC_DIR)

import unittest

from task1.src.is_a_heap import is_a_heap

class TestIsAHeap(unittest.TestCase):

    def test_should_check_the_possibility_of_identifying_if_test_1_array_is_a_heap(self):
        # given
        n = 5
        array = [1, 0, 1, 2, 0]
        expected_result = "NO"

        # when
        result = is_a_heap(array)

        # then
        self.assertEqual(result, expected_result)

    def test_should_check_the_possibility_of_identifying_if_test_2_array_is_a_heap(self):
        # given
        n = 5
        array = [1, 3, 2, 5, 4]
        expected_result = "YES"

        # when
        result = is_a_heap(array)

        # then
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()