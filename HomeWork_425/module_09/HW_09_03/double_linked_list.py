class Node:
    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_head(self, data):
        new_node = Node(data)
        if self.head is None:
            self.tail = new_node
        else:
            new_node.next_node = self.head  # работа с текущей головой
            self.head.prev_node = new_node  # работа с текущей головой
        self.head = new_node
        return f"Теперь в голове узел с данными {self.head.data}"

    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            # return self.insert_at_head(data)
            self.head = new_node
        else:
            self.tail.next_node = new_node
            new_node.prev_node = self.tail
        self.tail = new_node
        return f"Теперь в хвосте узел с данными {self.tail.data}"

    def remove_from_head(self):
        removed_node = self.head
        self.head = self.head.next_node
        self.head.prev_node = None
        return f"Были удалены данные {removed_node.data} из головы списка.\nТеперь голова списка {self.head.data}"

    def remove_from_tail(self):
        removed_node = self.tail
        self.tail = self.tail.prev_node
        self.tail.next_node = None
        return f"Были удалены данные {removed_node.data} из хвоста списка.\nТеперь хвост списка {self.tail.data}"

    def print_ll_from_head(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next_node
        return "Список выведен с начала"

class DoubleLinkedList(LinkedList):

    def print_ll_from_tail(self):
        current_node = self.tail
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.prev_node
        return "Список выведен с конца"

    def insert_at_index(self, index, data):
        new_node = Node(data)
        if index == 0:
            self.insert_at_head(data)
            return f"Узел с данными {new_node.data} добавлен в начало списка"

        current = self.head
        current_index = 0

        while current and current_index < index - 1:
            current = current.next_node
            current_index += 1

        if current:
            new_node.next_node = current.next_node
            new_node.prev_node = current

            if current.next_node:
                current.next_node.prev_node = new_node
            else:
                self.tail = new_node

            current.next_node = new_node
            return f"Узел с данными {new_node.data} добавлен"
        else:
            self.tail.next_node = new_node
            new_node.prev_node = self.tail
            self.tail = new_node
            return f"Узел с данными {new_node.data} добавлен в конце списка"

    def remove_node_index(self, index):
        if index < 0 or not self.head:
            return "Ничего не удалено"

        current = self.head
        current_index = 0

        while current and current_index < index:
            current = current.next_node
            current_index += 1

        if not current:
            return  "Ничего не удалено"

        if current.prev_node:
            current.prev_node.next_node = current.next_node
        else:
            self.head = current.next_node

        if current.next_node:
            current.next_node.prev_node = current.prev_node
        else:
            self.tail = current.prev_node
        return f"Удален узел с индексом {index}"


    def remove_node_data(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev_node:
                    current.prev_node.next_node = current.next_node
                else:
                    self.head = current.next_node

                if current.next_node:
                    current.next_node.prev_node = current.prev_node
                else:
                    self.tail = current.prev_node

                return f"Удален узел с данными {data}"

            current = current.next_node
        return "Ничего не удалено"

    def len_ll(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next_node
        return count

    def contains_from_head(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next_node
        return False

    def contains_from_tail(self, data):
        current = self.tail
        while current:
            if current.data == data:
                return True
            current = current.prev_node
        return False

    def contains_from(self, data, from_tail=False):
        if from_tail:
            return self.contains_from_tail(data)
        return self.contains_from_head(data)



my_list = DoubleLinkedList()
my_list.insert_at_head("num_2")
my_list.insert_at_tail("num_4")
print(my_list.insert_at_index(0, "num_1"))
print(my_list.insert_at_index(5, "num_5"))
print(my_list.insert_at_index(2, "num_3"))
my_list.print_ll_from_tail()
print(my_list.remove_node_index(2))
print(my_list.remove_node_index(10))
my_list.print_ll_from_tail()
print(my_list.remove_node_data("num_5"))
my_list.print_ll_from_tail()
print(my_list.len_ll())
print(my_list.contains_from_head("num_2"))