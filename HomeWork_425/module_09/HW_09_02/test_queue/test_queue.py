import unittest
from Queue import Queue

class TestQueue(unittest.TestCase):
    queue_test = Queue()

    def test_1_is_empty(self):
        self.assertEqual(self.queue_test.is_empty(), True)
        self.queue_test.enqueue("num1")
        self.queue_test.enqueue("num2")
        self.queue_test.enqueue("num3")
        self.assertEqual(self.queue_test.is_empty(), False)

    def test_2_is_full(self):
        self.assertEqual(self.queue_test.is_full(), True)
        self.queue_test.dequeue()
        self.queue_test.dequeue()
        self.queue_test.dequeue()
        self.assertEqual(self.queue_test.is_full(), False)