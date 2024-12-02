import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', '..')
sys.path.insert(0, src_dir)

import unittest

from task3.src.scarecrow_sort import scarecrow_sort


class TestScarecrowSort(unittest.TestCase):

    def test_should_check_the_possibility_of_sorting_example1_array(self):
        # given
        n, k = 3, 2
        array = [2, 1, 3]
        expected_result = 'NO'

        # when
        result = scarecrow_sort(n, k, array)

        # then
        self.assertEqual(result, expected_result)

    def test_should_check_the_possibility_of_sorting_example2_array(self):
        # given
        n, k = 5, 3
        array = [1, 5, 3, 4, 1]
        expected_result = 'YES'
        # when
        result = scarecrow_sort(n, k, array)

        # then
        self.assertEqual(result, expected_result)

    def test_should_check_the_possibility_of_sorting_sorted_array(self):
        # given
        n, k = 5, 3
        array = [1, 2, 3, 4, 5]
        expected_result = 'YES'

        # when
        result = scarecrow_sort(n, k, array)

        # then
        self.assertEqual(result, expected_result)

    def test_should_check_the_possibility_of_sorting_reverse_sorted_array(self):
        # given
        n, k = 5, 3
        array = [5, 4, 3, 2, 1]
        expected_result = 'NO'

        # when
        result = scarecrow_sort(n, k, array)

        # then
        self.assertEqual(result, expected_result)

    def test_should_check_the_possibility_of_sorting_single_element_array(self):
        # given
        n, k = 1, 3
        array = [1]
        expected_result = 'YES'

        # when
        result = scarecrow_sort(n, k, array)

        # then
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()