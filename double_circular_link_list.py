class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleCircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            temp = self.head.prev
            temp.next = new_node
            new_node.prev = temp
            new_node.next = self.head
            self.head.prev = new_node

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            temp = self.head.prev
            temp.next = new_node
            new_node.prev = temp
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self, key):
        if not self.head:
            return
        current = self.head
        while True:
            if current.data == key:
                if current.next == self.head:
                    if current.prev == self.head:  # Only one node in the list
                        self.head = None
                    else:  # Last node in the list
                        current.prev.next = self.head
                        self.head.prev = current.prev
                        self.head = current.next
                else:
                    if current == self.head:  # Head node
                        self.head = current.next
                    current.prev.next = current.next
                    current.next.prev = current.prev
                return
            current = current.next
            if current == self.head:
                break

    def print_list(self):
        if not self.head:
            return
        temp = self.head
        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.head:
                break
        print()

# Example Usage:
dcll = DoubleCircularLinkedList()
dcll.append(1)
dcll.append(2)
dcll.append(3)
dcll.prepend(0)
dcll.print_list()  # Output: 0 1 2 3

dcll.delete(2)
dcll.print_list()  # Output: 0 1 3
