import unittest
from Stack import Node, Stack

class TestNode(unittest.TestCase):

    def test_Node(self):
        node_1 = Node(5)
        self.assertEqual(node_1.data, 5)
        self.assertEqual(node_1.next_node, None)
        node_2 = Node(3, node_1)
        self.assertEqual(node_2.data, 3)
        self.assertEqual(node_2.next_node, node_1)

class TestStack(unittest.TestCase):
    stack_test = Stack(2)

    def test_1_init(self):
        self.assertEqual(self.stack_test.top, None)
        self.assertEqual(self.stack_test.stack_size, 2)

    def test_2_push(self):
        self.stack_test.push('test_data1')
        self.stack_test.push('test_data2')
        self.assertEqual(self.stack_test.top.data, 'test_data2')
        self.assertEqual(self.stack_test.top.next_node.data, 'test_data1')
        self.assertEqual(self.stack_test.push('test_data3'), 'Стэк переполнен')

    def test_3_pop(self):
        self.stack_test.clear_stack()
        self.stack_test.push('test_data')
        self.assertEqual(self.stack_test.pop(), 'test_data')
        self.assertEqual(self.stack_test.top, None)

    def test_4_is_empty(self):
        self.assertEqual(self.stack_test.is_empty(), True)
        self.stack_test.push('test_data')
        self.assertEqual(self.stack_test.is_empty(), False)

    def test_5_is_full(self):
        self.assertEqual(self.stack_test.is_full(), False)
        self.stack_test.push('test_data1')
        self.assertEqual(self.stack_test.is_full(), True)

    def test_6_clear_stack(self):
        self.stack_test.clear_stack()
        self.assertEqual(self.stack_test.is_empty(), True)

    def test_7_get_data(self):
        self.stack_test.push(1)
        self.stack_test.push('test_data')
        self.assertEqual(self.stack_test.get_data(0), "test_data")
        self.assertEqual(self.stack_test.get_data(5), "Out of range")

    def test_8_size_stack(self):
        self.assertEqual(Stack.size_stack(self.stack_test), 2)

    def test_9_counter_int(self):
        self.assertEqual(Stack.counter_int(self.stack_test), 1)





