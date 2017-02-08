'''
Print Left View of a Binary Tree
Left view of a Binary Tree is set of nodes visible when tree is visited from left side.
Left view of following tree is 12, 10, 25.
          12
       /     \
     10       20
            /    \
          25      40
The left view contains all nodes that are first nodes in their levels.

A simple solution is to do level order traversal and print the first node in every level.

The problem can also be solved using simple recursive traversal.
We can keep track of level of a node by passing a parameter to all recursive calls.
The idea is to keep track of maximum level also.
Whenever we see a node whose level is more than maximum level so far,
we print the node because this is the first node in its level
(Note that we traverse the left subtree before right subtree).
'''

# A binary tree node
class Node:
    def __init__(self, data):   # Constructor to create a new node
        self.data = data
        self.left = None
        self.right = None


# Recursive function print left view of a binary tree
def leftViewUtil(root, level, max_level):
    if root is None:                                # Base Case
        return

    if (max_level[0] < level):                      # If this is the first node of its level
        print root.data,
        max_level[0] = level

    leftViewUtil(root.left, level+1, max_level)     # traverse the left subtree before right subtree
    leftViewUtil(root.right, level+1, max_level)


def leftView(root):
    max_level = [0]
    leftViewUtil(root, 1, max_level)                # A wrapper over leftViewUtil()

# Driver program to test above function
root = Node(12)
root.left = Node(10)
root.right = Node(20)
root.right.left = Node(25)
root.right.right = Node(40)

leftView(root)