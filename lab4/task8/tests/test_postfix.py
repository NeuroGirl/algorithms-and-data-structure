import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', '..')
sys.path.insert(0, src_dir)

import unittest

from task8.src.postfix_calc import postfix

class TestPostfixCalc(unittest.TestCase):

    def test_should_check_the_possibility_of_solving_example1_array(self):
        # given
        n = 7
        array = ["8", "9", "+", "1", "7", "-", "*"]
        expected_result = [-102]

        # when
        result = postfix(array)

        # then
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()