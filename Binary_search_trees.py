

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.right = None
#         self.left = None


# class Binary_search_tree:
#     def __init__(self):
#         self.root = None

#     def add_node(self):
#         val = int(input("Enter value you want to add:"))
#         if self.root is None:
#             self.root = Node(val)
#             print("Node added")
#         else:
#             new = self.root
#             while new is not None:
#                 if val > new.data and new.right is None:
#                     new.right = Node(val)
#                     print("node added")
#                     break
#                 elif val > new.data and new.right is not None:
#                     new = new.right
#                     continue
#                 elif val < new.data and new.left is None:
#                     new.left = Node(val)
#                     print('node added')
#                     break
#                 else:
#                     new = new.left
#                     continue

#     def search_binary_tree(self, n, value):
#         if n is None:
#             print("no value in tree")
#         else:
#             new = self.root
#             while new is not None:
#                 if value == new.data:
#                     print("value found")
#                     return True
#                 elif value > new.data:
#                     new = new.right
#                     continue
#                 elif value < new.data:
#                     new = new.left
#                     continue
#             print("value not found")

#     def delete_node(self, value, root):
#         if root is None:
#             #print(f"Value {value} not found in the tree")
#             return None, False

#         if value < root.data:
#             root.left, found = self.delete_node(value, root.left)

#             return root, found
#         elif value > root.data:
#             root.right, found = self.delete_node(value, root.right)

#             return root, found
#         else:
#             if root.left is None:
#                 temp = root.right
#                 root = None
#                 return temp, True
#             elif root.right is None:
#                 temp = root.left
#                 root = None
#                 return temp, True

#             temp = self.find_min(root.right)
#             root.data = temp.data

#             root.right, found = self.delete_node(temp.data, root.right)
#             return root, found
#             # temp = self.find_max(root.left)
#             # root.data = temp.data
#             # root.right = self.delete_node(temp.data,root.left)

#         return root

#     def find_min(self, node):
#         current = node
#         while current.left is not None:
#             current = current.left
#         return current

#     def find_max(self, node):
#         current = node
#         while current.right is not None:
#             current = current.right
#         return current

#     def in_order(self, n):

#         if n is None:

#             return
#         else:
#             self.in_order(n.left)
#             print(n.data, end="-->")
#             self.in_order(n.right)

#     def pre_order(self, n):

#         if n is None:
#             return
#         else:
#             print(n.data, end="-->")
#             self.pre_order(n.left)
#             self.pre_order(n.right)

#     def post_order(self, n):
#         if n is None:
#             return
#         else:
#             self.post_order(n.left)
#             self.post_order(n.right)
#             print(n.data, end="-->")




# obj1 = Binary_search_tree()
# inputs = int(input("enter amount of nodes you want to add:"))
# for i in range(inputs):
#     obj1.add_node()
# a = obj1.root
# num = int(input("Enter value you want to delete:"))
# found = obj1.delete_node(num, a)
# print(found)
# if not found:
#      print(f"Value {num} not found in the tree")
# else:
#     print(f'value {num} found in tree')
# print("_______Inorder traversal_______")
# obj1.in_order(a)
# print()
# print("_______Preorder traversal_______")
# obj1.pre_order(a)
# print()
# print("_______Postorder traversal_______")
# obj1.post_order(a)
# print()

# val = int(input("Enter value you want to search in tree:"))
# obj1.search_binary_tree(a, val)
class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class Binary_search_tree:
    def __init__(self):
        self.root = None

    def add_node(self, val):
        if self.root is None:
            self.root = Node(val)
            print("Node added")
        else:
            new = self.root
            while new is not None:
                if val > new.data and new.right is None:
                    new.right = Node(val)
                    print("Node added")
                    break
                elif val > new.data and new.right is not None:
                    new = new.right
                elif val < new.data and new.left is None:
                    new.left = Node(val)
                    print("Node added")
                    break
                else:
                    new = new.left

    def search_binary_tree(self, n, value):
        if n is None:
            print("No value in tree")
        else:
            new = self.root
            while new is not None:
                if value == new.data:
                    print("Value found")
                    return True
                elif value > new.data:
                    new = new.right
                else:
                    new = new.left
            print("Value not found")
            return False

    def delete_node(self, value, root):
        if root is None:
            return None, False

        if value < root.data:
            root.left, found = self.delete_node(value, root.left)
            return root, found
        elif value > root.data:
            root.right, found = self.delete_node(value, root.right)
            return root, found
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp, True
            elif root.right is None:
                temp = root.left
                root = None
                return temp, True

            temp = self.find_min(root.right)
            root.data = temp.data
            root.right, found = self.delete_node(temp.data, root.right)
            return root, found

    def find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def find_max(self, node):
        current = node
        while current.right is not None:
            current = current.right
        return current

    def in_order(self, n):
        if n is not None:
            self.in_order(n.left)
            print(n.data, end="-->")
            self.in_order(n.right)

    def pre_order(self, n):
        if n is not None:
            print(n.data, end="-->")
            self.pre_order(n.left)
            self.pre_order(n.right)

    def post_order(self, n):
        if n is not None:
            self.post_order(n.left)
            self.post_order(n.right)
            print(n.data, end="-->")

# Example usage
obj1 = Binary_search_tree()
inputs = int(input("Enter number of nodes you want to add: "))
for i in range(inputs):
    val = int(input(f"Enter value for node {i + 1}: "))
    obj1.add_node(val)

a = obj1.root
num = int(input("Enter value you want to delete: "))
root, found = obj1.delete_node(num, a)
if not found:
    print(f"Value {num} not found in the tree")
else:
    print(f"Value {num} deleted from the tree")

print("_______Inorder traversal_______")
obj1.in_order(root)
print()
print("_______Preorder traversal_______")
obj1.pre_order(root)
print()
print("_______Postorder traversal_______")
obj1.post_order(root)
print()

val = int(input("Enter value you want to search in tree: "))
obj1.search_binary_tree(root, val)
