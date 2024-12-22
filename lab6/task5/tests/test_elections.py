import sys
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(CURRENT_DIR, '..', '..')
sys.path.insert(0, SRC_DIR)

import unittest

from task5.src.elections import count_votes

class TestElections(unittest.TestCase):

    def test_should_check_the_results_of_the_first_elections(self):
        # given
        array = ['McCain', '10', 'McCain', '5', 'Obama', '9', 'Obama', '8', 'McCain', '1']
        expected_result = ['McCain 16\n', 'Obama 17\n']

        # when
        result = count_votes(array)

        # then
        self.assertEqual(result, expected_result)

    def test_should_check_the_results_of_the_second_elections(self):
        # given
        array = ['Ivanov', '100', 'Ivanov', '500', 'Ivanov', '300', 'Petrov', '70', 'tourist', '1', 'tourist', '2']
        expected_result = ['Ivanov 900\n', 'Petrov 70\n', 'tourist 3\n']

        # when
        result = count_votes(array)

        # then
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()