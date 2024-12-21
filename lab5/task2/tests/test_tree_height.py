import sys
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(CURRENT_DIR, '..', '..')
sys.path.insert(0, SRC_DIR)

import unittest

from task2.src.tree_height import tree_height

class TestTreeHeight(unittest.TestCase):

    def test_should_check_the_possibility_of_measuring_the_depth_of_the_1st_heap(self):
        # given
        n = 5
        array = [4, -1, 4, 1, 1]
        expected_result = 3

        # when
        result = tree_height(n, array)

        # then
        self.assertEqual(result, expected_result)

    def test_should_check_the_possibility_of_measuring_the_depth_of_the_2nd_heap(self):
        # given
        n = 5
        array = [-1, 0, 4, 0, 3]
        expected_result = 4

        # when
        result = tree_height(n, array)

        # then
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()