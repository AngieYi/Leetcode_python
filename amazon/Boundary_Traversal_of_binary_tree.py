'''
Boundary Traversal of binary tree
Given a binary tree, print boundary nodes of the binary tree Anti-Clockwise starting from the root.
For example, boundary traversal of the following tree is: 20 8 4 10 14 25 22
                  20
                /   \
               8     22
            /	\     \
           4    12    25
              /   \
             10   14

We break the problem in 3 parts:
1. Print the left boundary in top-down manner.
2. Print all leaf nodes from left to right, which can again be sub-divided into two sub-parts:
    2.1 Print all leaf nodes of left sub-tree from left to right.
    2.2 Print all leaf nodes of right subtree from left to right.
3. Print the right boundary in bottom-up manner.

We need to take care of one thing that nodes are not printed again.
e.g.The left most node is also the leaf node of the tree.
'''

# A binary tree node
class Node:
	def __init__(self, data):
		self.data = data	# Constructor to create a new node
		self.left = None
		self.right = None

# Print leaf nodes of a Binary Tree
def printLeaves(root):
	if root:
		printLeaves(root.left)
		if not root.left and not root.right: # if it's a leaf node
			print root.data,   # with/without,, that's different
		printLeaves(root.right)

# print all left boundary nodes, except a leaf node.
# print the nodes in TOP DOWN manner
def printBoundaryLeft(root):
	if root:
		if root.left:
			print root.data,	# to ensure top down order, print node before calling left subtree
			printBoundaryLeft(root.left)
		elif root.right:
			print root.data,
			printBoundaryRight(root.right)
		# if it's a leaf node, do nothing.
		# so that avoid duplicates in output

# print all right boundary nodes, except a leaf node.
# Print the nodes in BOTTOM UP manner
def printBoundaryRight(root):
	if root:
		if root.right:
			printBoundaryRight(root.right) # to ensure bottom up order, call right subtree before print node
			print root.data,
		elif root.left:
			printBoundaryRight(root.left)
			print root.data,
		# if it's a leaf node,do nothing,
		# so that we avoid duplicates in output

# do boundary traversal of a given binary tree
def printBoundary(root):
	if root:
		print root.data,
		printBoundaryLeft(root.left)   # print the left boundary in top-down manner
		printLeaves(root.left)		   # print all leaf nodes
		printLeaves(root.right)
		printBoundaryRight(root.right) # print the right boundary in bottom-up manner

root = Node(20)
root.left = Node(8)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
root.right = Node(22)
root.right.right = Node(25)
printBoundary(root)