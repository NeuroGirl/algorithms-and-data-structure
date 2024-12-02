import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', '..')
sys.path.insert(0, src_dir)

import unittest

from task6.src.minimum_queue import queue_func_min

class TestMinimumQueue(unittest.TestCase):

    def test_should_check_the_possibility_of_solving_example1_array(self):
        # given
        n = 7
        array = ["+1", "?", "+10", "?", "-", "?", "-"]
        expected_result = ["1\n", "1\n", "10\n"]

        # when
        result = queue_func_min(array)

        # then
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()