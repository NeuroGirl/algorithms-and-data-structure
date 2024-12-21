import sys
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(CURRENT_DIR, '..', '..')
sys.path.insert(0, SRC_DIR)

import unittest

from task4.src.pyramid_build import create_heap

class TestPyramidBuild(unittest.TestCase):

    def test_should_check_the_possibility_of_searching_inversions_on_1st_heap(self):
        # given
        n = 5
        array = [5, 4, 3, 2, 1]
        expected_result = ['1 4\n', '0 1\n', '1 3\n']

        # when
        result = create_heap(n, array)

        # then
        self.assertEqual(result, expected_result)

    def test_should_check_the_possibility_of_measuring_the_depth_of_the_2nd_heap(self):
        # given
        n = 5
        array = [1, 2, 3, 4, 5]
        expected_result = []

        # when
        result = create_heap(n, array)

        # then
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()