import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', '..')
sys.path.insert(0, src_dir)

import unittest

from task1.src.merge_sort import sort_merge


class TestSortMerge(unittest.TestCase):

    def test_should_create_check_sorting_1st_array(self):
        # given
        array = ["2", "3", "4", "7", "5"]

        # when
        result = sort_merge(array)
        expected_result = ['2', '3', '4', '5', '7']

        # then
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()