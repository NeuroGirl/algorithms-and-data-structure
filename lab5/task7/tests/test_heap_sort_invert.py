import sys
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(CURRENT_DIR, '..', '..')
sys.path.insert(0, SRC_DIR)

import unittest

from task7.src.heap_sort_invert import heap_sort

class TestHeapSortInvert(unittest.TestCase):

    def test_should_check_the_possibility_of_sorting_1st_array(self):
        # given
        array = [1, 0, 1, 2, 0]
        expected_result = [2, 1, 1, 0, 0]

        # when
        result = heap_sort(array)

        # then
        self.assertEqual(result, expected_result)

    def test_should_check_the_possibility_of_sorting_2nd_array(self):
        # given
        array = [1, 3, 2, 5, 4]
        expected_result = [5, 4, 3, 2, 1]

        # when
        result = heap_sort(array)

        # then
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()