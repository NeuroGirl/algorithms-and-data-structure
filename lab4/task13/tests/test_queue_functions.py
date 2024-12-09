import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', '..')
sys.path.insert(0, src_dir)

import unittest

from lab4.task13.src.queue_functions import *

class TestQueueFunctions(unittest.TestCase):
        # given
        # when
    def setUp(self):
        self.queue = Queue(3)

    def test_should_check_success_of_queue_empty(self):
        # then
        self.assertEqual(self.queue.isEmpty(), True)
        self.assertEqual(self.queue.peek(), None)
        self.assertEqual(self.queue.queue_size(), 0)

    def test_should_check_success_of_queue_enqueue(self):
        # given
        # when
        self.queue.enqueue(10)
        # then
        self.assertEqual(self.queue.isEmpty(), False)
        self.assertEqual(self.queue.peek(), 10)
        self.assertEqual(self.queue.queue_size(), 1)

    def test_should_check_success_of_queue_dequeue(self):
        # given
        # when
        self.queue.dequeue()
        # then
        self.assertEqual(self.queue.isEmpty(), True)
        self.assertEqual(self.queue.peek(), None)
        self.assertEqual(self.queue.queue_size(), 0)
        self.assertEqual(self.queue.dequeue(), 'Очередь пуста')

    def test_should_check_success_of_queue_full(self):
        # given
        # when
        self.queue.enqueue(20)
        self.queue.enqueue(10)
        self.queue.enqueue(30)
        # then
        self.assertEqual(self.queue.isFull(), True)
        self.assertEqual(self.queue.enqueue(60), 'Очередь переполнена')

if __name__ == '__main__':
    unittest.main()
