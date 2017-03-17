'''
Given a linked list, determine if it has a cycle in it.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
Multiple pointers having different steps are our friend to solve Linked List problems.
We can set two pointers to "run through" the linked list.
Since they have different pace, if the list is cyclic, they must meet after the starting point.
'''

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head
        while slow and fast and fast.next:
            slow = slow.next                # Step of 1
            fast = fast.next.next           # Setp of 2
            if slow is fast:                # Checking whether two pointers meet
                return True
        return False