"""
Reverse a singly linked list.
Hint:
A linked list can be reversed either iteratively or recursively. 
Could you implement both?
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, next):
        self.val = x
        self.next = next

class Solution(object):
    def reverseList2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev, nxt = None, None
        curr = head
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        head = prev
        return head

# test   stunog
node6 = ListNode('g', None)
node5 = ListNode('0', node6)
node4 = ListNode('n', node5)
node3 = ListNode('u', node4)
node2 = ListNode('t', node3)
head = ListNode('5', node2)

def display(headNode):
    while headNode != None:
        print(headNode.val, end = '->'),
        headNode = headNode.next
    print('None')

print("original singly linked list:")
display(head)
s = Solution()
newHead = s.reverseList2(head)
print("singly linked list after reversal:")
display(newHead)


