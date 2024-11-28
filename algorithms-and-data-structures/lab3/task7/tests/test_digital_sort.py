import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', '..')
print(src_dir)
sys.path.insert(0, src_dir)

import unittest
from task7.src.digital_sort import radix_sort_phase


class TestRadixSort(unittest.TestCase):

    def test_should_make_radix_sort_phase(self):
        # given
        strings = [
            (1, "abc"),
            (2, "acd"),
            (3, "bcd")
        ]

        # when
        sorted_strings_phase_2 = radix_sort_phase(strings, 2)

        # then
        self.assertEqual(sorted_strings_phase_2, [
            (1, "abc"),
            (2, "acd"),
            (3, "bcd")
        ])

        # when
        sorted_strings_phase_1 = radix_sort_phase(strings, 1)

        # then
        self.assertEqual(sorted_strings_phase_1, [
            (1, "abc"),
            (2, "acd"),
            (3, "bcd")
        ])


if __name__ == '__main__':
    unittest.main()