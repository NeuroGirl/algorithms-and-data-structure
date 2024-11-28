import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', '..')
print(src_dir)
sys.path.insert(0, src_dir)

import unittest

from task2.src.quick_sort_desolver import anti_quick_sort


class TestAntiQuickSort(unittest.TestCase):

    def test_should_create_check_permutation_of_n_nums(self):
        # given
        # example n
        n1 = 3
        expected_result1 = [1, 3, 2]

        # another average n
        n2 = 10
        expected_result2 = [1, 4, 6, 8, 10, 5, 3, 7, 2, 9]

        # when
        result1 = anti_quick_sort(n1)
        result2 = anti_quick_sort(n2)

        # then
        self.assertEqual(result1, expected_result1)
        self.assertEqual(result2, expected_result2)


if __name__ == '__main__':
    unittest.main()