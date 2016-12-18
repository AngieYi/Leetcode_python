class Solution(object):
    def maxDepth1(self, root): # slower, Runtime: 102 ms
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        elif root.left and not root.right:
            return self.maxDepth(root.left) + 1  # when do recursive, use self.maxDepth, rather than maxDepth
        elif root.right and not root.left:
            return self.maxDepth(root.right) + 1
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    def maxDepth(self, root): # faster, Runtime: 65 ms
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        if root.left == None and root.right  == None:
            return 1
        elif root.left and root.right == None:
            return self.maxDepth(root.left) + 1  # when do recursive, use self.maxDepth, rather than maxDepth
        elif root.right and root.left == None:
            return self.maxDepth(root.right) + 1
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    def maxDepth(self, root): # Medium, Runtime: 72 ms
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

'''
Test case explanation
[]
Empty tree.
The root is a reference to NULL (C/C++), null (Java/C#/Javascript), None (Python), or nil (Ruby).

[1,2,3]
       1
      / \
     2   3

[1,null,2,3]
       1
        \
         2
        /
       3

[5,4,7,3,null,2,null,-1,null,9]
       5
      / \
     4   7
    /   /
   3   2
  /   /
 -1  9
'''

'''
what's the difference between not x and x == None?
not x will also return True for everything that evaluates to False in a boolean context.
Some examples:
>>> x = ()
>>> not x
True

>>> x = []
>>> not x
True

>>> x = ''
>>> not x
True

>>> x = 0
>>> not x
True

>>> x is None
False

So if your code should act differently when x is None as opposed to x being an empty list,
tuple, string, the number zero, ...
then use x == None or x is None instead of not x
'''