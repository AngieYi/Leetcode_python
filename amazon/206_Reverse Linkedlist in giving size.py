'''
Reverse a Linked List in groups of given size
Given a linked list, write a function to reverse every k nodes (where k is an input to the function).

Example:
Inputs:  1->2->3->4->5->6->7->8->NULL and k = 3
Output:  3->2->1->6->5->4->8->7->NULL.

Inputs:   1->2->3->4->5->6->7->8->NULL and k = 5
Output:  5->4->3->2->1->8->7->6->NULL.


Algorithm: reverse(head, k)
The difference between Q1: Reverse a Linked List and Q2: Reverse a Linked List in groups of given size
Q1 is actually the sub-problem of Q2.
The sub problem is how to reverse a k-length list.
After knowing the sub-problem, the left question is how to connect each reversed sub-list.
1) After finishing k length of elements, need to save the tail(the head at the beginning),
   because you need use this tail to connect to the next section.
2) each section could be called recursively.
'''


class Node:
    def __init__(self, data):    # Constructor to initialize the node object
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):          # Function to initialize head
        self.head = None

    def reverse(self, head, k):
        tail = head              # save the tail of current section
        pre = None
        count = 0

        while head and count < k:
            cur = head
            head = head.next
            cur.next = pre
            pre = cur
            count += 1

        if head:
            tail.next = self.reverse(head, k)   # connect current section with next section

        return pre     # pre is new head of current section

    def push(self, new_data):       # insert a new node at the beginning
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):            # print the LinkedList
        temp = self.head
        while temp:
            print temp.data,
            temp = temp.next

llist = LinkedList()                # Driver program
llist.push(9)
llist.push(8)
llist.push(7)
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)

print "Given linked list"
llist.printList()
llist.head = llist.reverse(llist.head, 3)

print "\nReversed Linked list"
llist.printList()