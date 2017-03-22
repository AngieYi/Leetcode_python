'''
Write a program to find the node at which the intersection of two singly linked lists begins.
For example, the following two linked lists:
A:        a1 a2 c1 c2 c3
B:     b1 b2 b3 c1 c2 c3
begin to intersect at node c1.
Notes:
If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # 416ms 77.83%
        # 1. get the length of A,B
        curA,curB = headA,headB
        lenA,lenB = 0,0
        while curA:
            lenA += 1
            curA = curA.next
        while curB:
            lenB += 1
            curB = curB.next

        # 2. find the start position of the longer list
        curA,curB = headA,headB
        if lenA > lenB:
            for i in range(lenA-lenB):
                curA = curA.next
        elif lenB > lenA:
            for i in range(lenB-lenA):
                curB = curB.next

        # 3. compare and get the intersection start position
        while curB != curA:
            curB = curB.next
            curA = curA.next
        return curA