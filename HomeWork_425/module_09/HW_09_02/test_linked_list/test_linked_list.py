import unittest
from LinkedListClass import Node, LinkedList


class TestNode(unittest.TestCase):

    def test_Node(self):
        node_1 = Node(5)
        self.assertEqual(node_1.data, 5)
        self.assertEqual(node_1.next_node, None)
        node_2 = Node(3, node_1)
        self.assertEqual(node_2.data, 3)
        self.assertEqual(node_2.next_node, node_1)

class TestLinkedList(unittest.TestCase):
    test_list = LinkedList()

    def test_1_init(self):
        self.assertEqual(self.test_list.head, None)

    def test_2_insert_at_head(self):
        self.assertEqual(self.test_list.insert_at_head('num_2'), "Узел с данными num_2 добавлен в начало списка")
        self.assertEqual(self.test_list.insert_at_head('num_1'), "Узел с данными num_1 добавлен в начало списка")

    def test_3_insert_at_end(self):
        self.assertEqual(self.test_list.insert_at_end("num_3"), 'Узел с данными num_3 добавлен в конец списка')

    def test_4_remove_node_position(self):
        self.assertEqual(self.test_list.remove_node_position(2), 'Удален узел с данными num_2 позиции 2')

    def test_5_insert_at_position(self):
        self.assertEqual(self.test_list.insert_at_position("num_2", 2), "Узел с данными num_2 добавлен на позицию 2")

    def test_6_print_ll(self):
        self.assertEqual(self.test_list.print_ll(), "Данные списка выведены")

    def test_7_get(self):
        self.assertEqual(self.test_list.get('num_2'), True)
        self.assertEqual(self.test_list.get('num_4'), False)

    def test_8_change_data(self):
        self.assertEqual(self.test_list.change_data("num_2", "num_4"), 'Заменены данные в узле № 2')
        self.assertEqual(self.test_list.change_data("num", "num_4"), 'Данные не обнаружены')
