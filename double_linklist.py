class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def Add_at_tail(self, data):
        new_node = Node(data)
        if  self.head ==  None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def Add_at_head(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete_at_value(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                return
            current = current.next

    def add_sorted(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        elif data < self.head.data:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.data < data:
                current = current.next
            new_node.next = current.next
            if current.next:
                current.next.prev = new_node
            current.next = new_node
            new_node.prev = current

    def add_position(self, data, position):
        new_node = Node(data)
        if position <= 1:
            self.Add_at_head(data)
        else:
            current = self.head
            index = 1
            while current and index < position - 1:
                current = current.next
                index += 1
            if not current:
                print("Position out of bounds")
                return
            new_node.next = current.next
            if current.next:
                current.next.prev = new_node
            current.next = new_node
            new_node.prev = current

    def delete_head(self):
        if not self.head:
            print("List is empty")
        elif not self.head.next:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def delete_tail(self):
        if not self.head:
            print("List is empty")
        elif not self.head.next:
            self.head = None
        else:
            current = self.head
            while current.next:
                current = current.next
            current.prev.next = None

    def search_object(self, data_to_find):
        current = self.head
        index = 1
        while current:
            if current.data == data_to_find:
                print(f"Data '{data_to_find}' found at index: {index}")
                return
            current = current.next
            index += 1
        print(f"Data '{data_to_find}' not found in the list")
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


dll = DoublyLinkedList()
dll.Add_at_tail(1)
dll.Add_at_tail(3)
dll.Add_at_tail(5)
dll.Add_at_tail(7)
dll.Add_at_tail(9)
dll.Add_at_head(-1)
dll.display()
# dll.delete_head()
# dll.delete_tail()
# dll.add_sorted(2)
# dll.add_position(24,2)
# dll.search_object(24)
# dll.display()
