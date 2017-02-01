'''
230. Kth Smallest Element in a BST
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
Note: You may assume k is always valid, k is between 1 and BST's total elements.
Follow up: What if the BST is modified (insert/delete operations) often and
you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
Hint: Try to utilize the property of a BST.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # 78ms, 98.12%
    # iterative in order traversal
    def kthSmallest(self,root, k):
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()

            k -= 1
            if k == 0:
                return root.val

            root = root.right

    '''
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.k = k
        self.res = None
        self.helper(root)
        return self.res

    def helper(self, node):
        if not node:
            return
        self.helper(node.left)
        self.k -= 1
        if self.k == 0:
            self.res = node.val
            return
        self.helper(node.right)
    '''

    '''
    Method 2: Augmented  Tree Data Structure.
    The idea is to maintain rank of each node.
    We can keep track of elements in a subtree of any node while building the tree.
    Since we need K-th smallest element, we can maintain number of elements of left subtree in every node.

    Assume that the root is having N nodes in its left subtree.
    If K = N + 1, root is K-th node.
    If K < N, we will continue our search (recursion) for the Kth smallest element in the left subtree of root.
    If K > N + 1, we continue our search in the right subtree for the (K – N – 1)-th smallest element.
    Note that we need the count of elements in left subtree only.

    Time complexity: O(h) where h is height of tree.
    http://www.geeksforgeeks.org/find-k-th-smallest-element-in-bst-order-statistics-in-bst/
    '''