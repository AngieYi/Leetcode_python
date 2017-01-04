'''
206. Reverse Linked List
Reverse a singly linked list.
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # 42ms: very clear head is ahead, cur is current, pre is previous
        pre = None
        while head:
            cur = head
            head = head.next
            cur.next = pre
            pre = cur
        return pre


        '''
        # 62ms: mine right but not clear
        if head == None:
            return head
        cur = head.next
        head.next = None
        while cur:
            post = cur.next
            cur.next = head
            head = cur
            cur = post
        return head
        '''