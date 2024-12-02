import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', '..')
sys.path.insert(0, src_dir)

import unittest

from task7.src.find_max import find_max


class TestFindMax(unittest.TestCase):

    def test_should_create_check_calculating_1st_array(self):
        # given
        mass = ['13', '-3', '-25', '20', '-3', '-16', '-23', '18', '10', '9', '20', '-7', '12', '-5', '-22', '15', '-4', '7']

        # when
        result = find_max(mass)
        expected_result = ['18', '10', '9', '20', '-7', '12']

        # then
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()