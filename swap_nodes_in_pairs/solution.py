# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """recursive method"""
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head is None or head.next is None:
            return head
        else:
            t = head.next
            head.next = self.swapPairs(t.next)# recursion begins from here
            t.next = head
            return t

# singly linked list  1->2->None

# head     t
# 1    ->  2 -> None
# 1    ->  None
# 2    ->  1  -> None

# test 
head = ListNode(1)
node1 = ListNode(2)
node2 = ListNode(3)
node3 = ListNode(4)
head.next = node1
node1.next = node2
node2.next = node3

def display(head):
    walk = head
    while walk != None:
        print (walk.val)
        walk = walk.next

display(head)
s = Solution()
newHead = s.swapPairs(head)
print("after swapping")
display(newHead)




