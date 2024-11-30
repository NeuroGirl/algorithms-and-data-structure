import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', '..')
sys.path.insert(0, src_dir)

import unittest

from task3.src.bracet_counter import bracet_counter_cycled

class TestBracetCounter(unittest.TestCase):

    def test_should_check_the_possibility_of_solving_example1_array(self):
        # given
        n = 4
        array = ["[())]", "", "[[[[]]]]", "(([[]))"]
        expected_result = ["NO\n", "YES\n", "YES\n", "NO\n"]

        # when
        result = bracet_counter_cycled(n, array)

        # then
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()