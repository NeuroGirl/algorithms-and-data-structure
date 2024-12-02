import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', '..')
sys.path.insert(0, src_dir)

import unittest

from task12.src.formation import formation

class TestFormation(unittest.TestCase):

    def test_should_check_the_possibility_of_solving_example1_array(self):
        # given
        n, m = 3, 4
        array = ["left 2 1", "right 3 1", "leave 1" ,"name 2"]
        expected_result = ["0 3"]

        # when
        result = formation(n, array)

        # then
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()