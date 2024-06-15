class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if not self.head:
            new_node.next = new_node
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
        self.head = new_node

    def delete(self, key):
        if not self.head:
            return
        if self.head.data == key:
            current = self.head
            while current.next != self.head:
                current = current.next
            if self.head == self.head.next:
                self.head = None
            else:
                current.next = self.head.next
                self.head = self.head.next
        else:
            current = self.head
            prev = None
            while current.next != self.head:
                prev = current
                current = current.next
                if current.data == key:
                    prev.next = current.next
                    current = current.next

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
cll = CircularLinkedList()
cll.append(1)
cll.append(2)
cll.append(3)
cll.prepend(0)
cll.print_list()  # Output: 0 1 2 3

cll.delete(2)
cll.print_list()  # Output: 0 1 3
