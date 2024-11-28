import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', '..')
sys.path.insert(0, src_dir)

import unittest

from task1.src.random_quick_sort import randomized_quick_sort
from utils import generate_random_array


class TestRandomizedQuickSort(unittest.TestCase):

    def test_should_sort_example_array(self):
        # given
        n = 5
        array = [2, 3, 9, 2, 2]
        expected_result = [2, 2, 2, 3, 9]

        # when
        result = randomized_quick_sort(array, 0, n - 1)

        # then
        self.assertEqual(result, expected_result)

    def test_should_sort_sorted_array(self):
        # given
        n = 6
        array = [1, 2, 3, 4, 5, 6]
        expected_result = [1, 2, 3, 4, 5, 6]

        # when
        result = randomized_quick_sort(array, 0, n - 1)

        # then
        self.assertEqual(result, expected_result)

    def test_should_sort_reverse_sorted_array(self):
        # given
        n = 6
        array = [6, 5, 4, 3, 2, 1]
        expected_result = [1, 2, 3, 4, 5, 6]

        # when
        result = randomized_quick_sort(array, 0, n - 1)

        # then
        self.assertEqual(result, expected_result)

    def test_should_sort_single_element_array(self):
        # given
        n = 1
        array = [0]
        expected_result = [0]

        # when
        result = randomized_quick_sort(array, 0, n - 1)

        # then
        self.assertEqual(result, expected_result)

    def test_should_sort_empty_array(self):
        # given
        n = 0
        array = []
        expected_result = []

        # when
        result = randomized_quick_sort(array, 0, len(array) - 1)

        # then
        self.assertEqual(result, expected_result)

    def test_should_sort_large_numbers_array(self):
        # given
        n = 10 ** 5
        array = generate_random_array(n, -10 ** 9, 10 ** 9)
        expected_result = sorted(array)

        # when
        result = randomized_quick_sort(array, 0, n - 1)

        # then
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()