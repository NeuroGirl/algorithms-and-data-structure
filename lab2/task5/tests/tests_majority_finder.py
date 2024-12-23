import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', '..')
sys.path.insert(0, src_dir)

import unittest

from task5.src.majority_finder import majority_finder


class TestMajorityFinder(unittest.TestCase):

    def test_should_create_check_calculating_1st_array(self):
        # given
        mass = ['2', '3', '9', '2', '2']

        # when
        result = majority_finder(mass)
        expected_result = 1

        # then
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()