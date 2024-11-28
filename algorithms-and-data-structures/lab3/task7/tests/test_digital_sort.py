import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', '..')
sys.path.insert(0, src_dir)

import unittest
from task7.src.digital_sort import radix_sort_phase

class TestRadixSort(unittest.TestCase):

    def test_should_make_radix_sort_phase(self):
        # given
        strings = [
            (1, "bab"),
            (2, "bba"),
            (3, "baa")
        ]
        # when
        sorted_strings_phase_2 = radix_sort_phase(strings, 1)

        # then
        self.assertEqual(sorted_strings_phase_2, [
            (1, "bab"),
            (3, "baa"),
            (2, "bba")
        ])

if __name__ == '__main__':
    unittest.main()
