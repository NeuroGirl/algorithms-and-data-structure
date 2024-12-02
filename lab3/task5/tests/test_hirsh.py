import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', '..')
sys.path.insert(0, src_dir)

import unittest

from task5.src.hirsh_index import hirsch_index


class TestHirschIndex(unittest.TestCase):

    def test_should_find_hirsch_index_example1_array(self):
        # given
        array = [3, 0, 6, 1, 5]
        expected_result = 3

        # when
        result = hirsch_index(array)

        # then
        self.assertEqual(result, expected_result)

    def test_should_find_hirsch_index_example2_array(self):
        # given
        array = [1, 3, 1]
        expected_result = 1

        # when
        result = hirsch_index(array)

        # then
        self.assertEqual(result, expected_result)

    def test_should_find_hirsch_index_sorted_array(self):
        # given
        array = [1, 2, 3, 4]
        expected_result = 2

        # when
        result = hirsch_index(array)

        # then
        self.assertEqual(result, expected_result)

    def test_should_find_hirsch_index_reverse_sorted_array(self):
        # given
        array = [4, 3, 2, 1]
        expected_result = 2

        # when
        result = hirsch_index(array)

        # then
        self.assertEqual(result, expected_result)

    def test_should_count_inversions_empty_array(self):
        # given
        array = []
        expected_result = 0

        # when
        result = hirsch_index(array)

        # then
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()