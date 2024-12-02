import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', '..')
sys.path.insert(0, src_dir)

import unittest

from task9.src.strassen import strassen_apply


class TestFindMax(unittest.TestCase):

    def test_should_create_check_calculating_1st_2_matrixes(self):
        # given
        dim = 2
        array1 = ['1', '2', '3', '4']
        array2 = ['9', '8', '7', '8']
        # when
        result = strassen_apply(dim, array1, array2)
        expected_result = [[[23, 24], [55, 56]]]

        # then
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()