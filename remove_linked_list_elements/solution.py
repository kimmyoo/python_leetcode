"""
Remove all elements from a linked list of integers 
that have value val.
Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, next):
        self.val = x
        self.next = next

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return None
        current = head
        last = None
        # e.g. remove 'w' 
        #   crt                                  lst = None
        #    h - w - e - l - l  - i - o - r -a 
        #   lst crt                              
        #    h - w - e - l - l  - i - o - r -a 
        #   lst     crt
        #    h - - - e - l - l  - i - o - r -a
        #           lst crt
        #    h - - - e - l - l  - i - o - r -a
        #    ......
        #                                lst crt
        #    h - - - e - l - l  - i - o - r -a
        #                                   lst  crt
        #    h - - - e - l - l  - i - o - r -a - None  while loop stops
        while current is not None:
            if current.val == val:
                if last is not None:
                    # Remove `current` node and `last` node is not changed
                    last.next = current.next
                else:
                    # `current` is the head node
                    # Remove the head node and `last` node is still None
                    head = current.next
                    last = None
            else:
                last = current
            current = current.next
        return head
        
# test
tail = ListNode('a', None)
node7 = ListNode('r', tail)
node6 = ListNode('o', node7)
node5 = ListNode('i', node6)
node4 = ListNode('l', node5)
node3 = ListNode('l', node4)
node2 = ListNode('e', node3)
node1 = ListNode('w', node2)
head = ListNode('h', node1)

def display(head):
    walk = head
    while walk != None:
        print (walk.val)
        walk = walk.next

print("original:")
display(head)

s = Solution()
s.removeElements(head, 'w')
s.removeElements(head, 'i')
s.removeElements(head, 'r')
s.removeElements(head, 'a')

print("after deletion:")
display(head)
    

