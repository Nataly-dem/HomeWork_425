"""Хранит узел с данными """
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

"""Класс очереди"""
class Queue:

    def __init__(self, head = None, tail=None, max_length = 3):
        self.head = head
        self.tail = tail
        self. max_length =  max_length
    """Добавляет элемент в очередь"""
    def enqueue(self, data):
        if self.is_full():
            print('Очередь заполнена')
            return 'Очередь заполнена'
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next_node = new_node
        self.tail = new_node

    """Удаление элемента из очереди"""
    def dequeue(self):
        if self.head is None:
            return None
        else:
            dequeue_item = self.head
            self.head = self.head.next_node
        return dequeue_item.data

    """подсчитывает количество элементов в очереди"""
    def get_queue_length(self):
        items_count = 0
        if self.head is None:
            return items_count
        temp_head = self.head
        while temp_head:
            items_count += 1
            temp_head = temp_head.next_node
        return items_count

    """Проверяет полное заполнение очереди"""
    def is_full(self):
        if self.max_length == self.get_queue_length():
            return True
        return False

    """проверяет очередь на пустоту"""
    def is_empty(self):
        if self.head is None:
            return True
        return False

    """Показывает все элементы в очереди"""
    def show(self):
        if not self.is_empty():
            temp_head = self.head
            while temp_head:
                print(temp_head.data)
                temp_head = temp_head.next_node
            return "Содержимое очереди показано"
        return "Очередь пуста"

#
# my_queue = Queue()
#
# my_queue.enqueue("num_1")
# my_queue.enqueue("num_2")
# my_queue.enqueue("num_3")
# my_queue.enqueue("num_4")
# print(my_queue.is_full())
# print(my_queue.show())
# print(my_queue.dequeue())
# print(my_queue.dequeue())
# print(my_queue.dequeue())
# print(my_queue.dequeue())

# print(my_queue.is_empty())



