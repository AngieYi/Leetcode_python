'''
203. Remove Linked List Elements
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        dummy = ListNode(-1)    # add a dummy node
        dummy.next = head       # head might be deleted if head.val == val

        cur = dummy             # cur is dynamic, always changing,like a temp pointer

        while cur != None and cur.next != None:     # first time cur.next is head
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy.next       # neither head nor cur, only dummy.next is right


        '''
        # wrong
        cur = head
        while cur != None:
            if cur.val == val and cur.next != None:
                cur = cur.next
            elif cur.val == val and cur.next == None:
                cur = None
            else:
                cur = cur.next
        return head
       '''
