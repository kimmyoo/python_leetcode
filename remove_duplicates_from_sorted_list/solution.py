"""
Given a sorted linked list, delete all duplicates such that each element
appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.

difficulty: *
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, next):
        self.val = x
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        if head.next is None:
            return head

        prev = head
        current = head.next
        while current is not None:
            next_node = current.next
            if current.val == prev.val:
                # skip current node， link prev to next_node
                prev.next = next_node
            else:
                prev = current
            current = next_node # move the current to next_node
        return head

# test code
tail = ListNode(9, None)
node4 = ListNode(9, tail)
node3 = ListNode(9, node4)
node2 = ListNode(6, node3)
node1 = ListNode(6, node2)
head = ListNode(3, node1)

def display(listHead):
    while listHead is not None:
        print (listHead.val)
        listHead = listHead.next

print ("Singly linked List before removal of duplicates:")
display(head)
s = Solution()
s.deleteDuplicates(head)
print ("after removal of duplicates:")
display(head)

