class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.arr = [None] * size

    def hash(self, key):
        hash_value = 0
        for char in key:
            hash_value += ord(char)
        return hash_value % self.size

    def add(self, value):
        key = self.hash(value)
        index = key
        if self.arr[index] is None:
            self.arr[index] = Node(key, value)
        else:
            current = self.arr[index]
            while current.next is not None:
                current = current.next
            current.next = Node(key, value)

    def search(self, key):
        index = self.hash(key)
        current = self.arr[index]
        while current is not None:
            if current.value == key:
                return f"Value found: {current.value}"
            current = current.next
        return "Value not found"

    def delete(self, key):
        index = self.hash(key)
        current = self.arr[index]
        if current is None:
            return "value not found, cannot delete"
        elif current.value == key:
            self.arr[index] = current.next
            return "value deleted successfully"
        else:
            prev = None
            while current is not None:
                if current.value == key:
                    prev.next = current.next
                    return "value deleted successfully"
                prev = current
                current = current.next
            return "value not found, cannot delete"

    def print_table(self):
        for i in range(self.size):
            print(f"Bucket {i}:", end=" ")
            current = self.arr[i]
            while current:
                print(f"({current.value})", end=" -> ")
                current = current.next
            print("None")
size = int(input("Enter size of hashtable:"))
hash_table = HashTable(size)
for ele in range(size):
    val = (input("Enter value:"))
    hash_table.add(val)
# hash_table.add("bom")
# hash_table.add("mob")
# hash_table.print_table()
#print(hash_table.search("mob"))
#
#print(hash_table.delete("banana"))
# print(hash_table.search("banana"))
