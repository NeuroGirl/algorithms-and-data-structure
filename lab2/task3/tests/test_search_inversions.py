import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', '..')
sys.path.insert(0, src_dir)

import unittest

from task3.src.search_inversions import search_inversions


class TestSortMerge(unittest.TestCase):

    def test_should_create_check_calculating_1st_array(self):
        # given
        n = 10
        array = ['1', '8', '2', '1', '4', '7', '3', '2', '3', '6']

        # when
        result = search_inversions(array, array, 0, n - 1)
        expected_result = 7

        # then
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()