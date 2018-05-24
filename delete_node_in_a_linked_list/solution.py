"""
Write a function to delete a node (except the tail) in a singly linked list,
given only access to that node.

Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node
with value 3, the linked list should become 1 -> 2 -> 4 after calling your
function.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, next):
        self.val = x
        self.next = next

# replace value with the value of the next node and point next to the 
# next of the next node
class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node.next is not None: # ensure the node to be deleted is not the tail
            node.val = node.next.val
            node.next = node.next.next

# test 
tail = ListNode(4, None)
node3 = ListNode(3, tail)
node2 = ListNode(2, node3)
head = ListNode(1, node2)

def displayList(walk):
    while walk is not None:
        print(walk.val)
        walk = walk.next
displayList(head)

s = Solution()
s.deleteNode(node3)
print("after deletion:")
displayList(head)
