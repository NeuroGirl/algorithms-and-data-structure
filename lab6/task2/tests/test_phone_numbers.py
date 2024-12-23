import sys
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(CURRENT_DIR, '..', '..')
sys.path.insert(0, SRC_DIR)

import unittest

from lab6.task2.src.phone_numbers import phone_book

class TestPhoneNumbers(unittest.TestCase):

    def test_should_check_the_possibility_of_search_in_the_1st_phone_book(self):
        # given
        array = ['add', '911', 'police', 'add', '76213', 'Mom', 'add', '17239', 'Bob', 'find', '76213', 'find', '910', 'find', '911', 'del', '910', 'del', '911', 'find', '911', 'find', '76213', 'add', '76213', 'daddy', 'find', '76213']
        expected_result = ['Mom\n', 'not found\n', 'police\n', 'not found\n', 'Mom\n', 'daddy\n']

        # when
        result = phone_book(array)

        # then
        self.assertEqual(result, expected_result)

    def test_should_check_the_possibility_of_of_search_in_the_2nd_phone_book(self):
        # given
        array = ['add', '76213', 'Chuuya', 'add', '17239', 'Hirotsu', 'find', '76213', 'find', '910', 'find', '911', 'del', '910', 'del', '911', 'find', '911', 'find', '76213', 'add', '76213', 'Mori', 'find', '76213']
        expected_result = ['Chuuya\n', 'not found\n', 'not found\n', 'not found\n', 'Chuuya\n', 'Mori\n']

        # when
        result = phone_book(array)

        # then
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()