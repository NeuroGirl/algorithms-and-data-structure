import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', '..')
sys.path.insert(0, src_dir)

import unittest

from task2.src.queue import queue_add_del

class TestQueue(unittest.TestCase):

    def test_should_check_the_possibility_of_sorting_example1_array(self):
        # given
        n = 4
        array = ["+1", "+10", "-", "-"]
        expected_result = ["1\n", "10\n"]

        # when
        result = queue_add_del(n, array)

        # then
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
