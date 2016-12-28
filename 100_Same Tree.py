'''
100. Same Tree
Given two binary trees, write a function to check if they are equal or not.
Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        '''
        # 48 ms
        if p == None and q == None:
            return True
        elif (p != None and q != None) and (p.val == q.val) and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right):
            return True
        else:
            return False
        '''

        # 35 ms
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q   # when p == None and q == None: (p is q) = True; otherwise (p is q) = False

        # 45 ms
        #return p and q and p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) or p is q

        # 39 ms
        #return p and q and p.val == q.val and all(map(self.isSameTree, (p.left, p.right), (q.left, q.right))) or p is q