from node import Node
from binary_tree import BinaryTree

tree = BinaryTree(Node(6))
# tree.add(Node(5))
# tree.add(Node(11))

# print(tree.head)
# print(tree.head.left)
# print(tree.head.right)

nodes = [5, 3, 9, 7, 8, 7.5, 12, 11]

for n in nodes:
    tree.add(Node(n))

tree.delete(9)
tree.inorder()

# tree.preorder()
