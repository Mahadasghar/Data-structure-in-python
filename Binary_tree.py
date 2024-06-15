class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class Binary_tree:
    count = 0
    t_count = 0

    def __init__(self):
        self.root = None

    def add_node(self):
        Binary_tree.t_count += 1
        data = int(input("Enter value you want to add:"))
        if self.root is None:
            self.root = Node(data)
            print("Node added")
        else:
            next = self.root
            while next is not None:
                inputs = int(input("If you want to add left node enter 0 and if right  enter 1:"))
                if inputs == 0:
                    if next.left is None:
                        next.left = Node(data)
                        print("Node added")
                        break
                    else:
                        next = next.left
                        continue
                else:
                    if next.right is None:
                        next.right = Node(data)
                        print("Node added")
                        break
                    else:
                        next = next.right
                        continue

    def in_order(self, n):

        if n is None:
            return
        else:
            self.in_order(n.left)
            print(n.data, end="-->")
            self.in_order(n.right)
    #
    # def printInorder(self,root):
    #
    #     if root is None:
    #         return
    #     else:
    #         # First recur on left child
    #         self.printInorder(root.left)
    #
    #         # Then print the data of node
    #         print(root.data, end=" "),
    #
    #         # Now recur on right child
    #         self.printInorder(root.right)
    def pre_order(self, n):

        if n is None:
            return
        else:
            print(n.data, end="-->")
            self.pre_order(n.left)
            self.pre_order(n.right)

    def post_order(self, n):
        if n is None:
            return
        else:
            self.post_order(n.left)
            self.post_order(n.right)
            print(n.data, end="-->")

    def search_element(self, n, value):
        #
        if n is None and Binary_tree.count != Binary_tree.t_count:
             return

        if n is None and Binary_tree.count == Binary_tree.t_count:
            print("Sorry 😢 value not found")
            return False



        else:
            Binary_tree.count += 1
            if n.data == value:
                print("Yahoo🎉🎉 Value found")
                return True

            self.search_element(n.left, value)

            self.search_element(n.right, value)





dll = Binary_tree()
inputs = int(input("enter amount of nodes you want to add:"))
for i in range(inputs):
    dll.add_node()

a = dll.root

print("_______Inorder traversal_______")
dll.in_order(a)
# dll.printInorder(a)
print()
# print("_______Preorder traversal_______")
# dll.pre_order(a)
# print()
# print("_______Postorder traversal_______")
# dll.post_order(a)
# print()
# val = int(input("Enter value you want to search in tree:"))
# dll.search_element(a, val)
