'''
234. Palindrome Linked List
Given a singly linked list, determine if it is a palindrome.
Follow up:
Could you do it in O(n) time and O(1) space?
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        # 139 ms
        #Phase 1: Reverse the first half while finding the middle.
        #Phase 2: Compare the reversed first half with the second half.
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next

        # len is even, slow stops at the first end, should move to the beginning of second part.
        # len is odd,slow and rev both are at middle, and then sperate at oppsite direction.
        if fast:
            slow = slow.next

        # if rev finally reaches the beginning, ==None, then they're symmetric
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next
        return not rev


        '''
        # 155ms

        # 1. find the middle
        # two start at the same place, slow's speed = 1/2 fast's speed, when fast finishes, slow is at middle
        # slow moves one step each time,while fast moves two steps each time
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # 2. reverse the second half
        # at the end, pre is the start node
        pre = None
        while slow:
            cur = slow
            slow = slow.next
            cur.next = pre
            pre = cur

        # 3. compare the first half with second half
        while head and pre:
            if head.val != pre.val:
                return False
            head = head.next
            pre = pre.next
        return True

        '''