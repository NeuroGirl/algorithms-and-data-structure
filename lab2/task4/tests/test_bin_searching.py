import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', '..')
sys.path.insert(0, src_dir)

import unittest

from task4.src.bin_searching import start_search


class TestBinSearching(unittest.TestCase):

    def test_should_create_check_calculating_1st_array(self):
        # given
        n = 5
        mass = ['1', '5', '8', '12', '13']
        k = 5
        mass_find = ['8', '1', '23', '1', '11']

        # when
        result = start_search(mass, mass_find)
        expected_result = [2, 0, -1, 0, -1]

        # then
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()