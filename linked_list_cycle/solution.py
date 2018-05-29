"""
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

# example: 
# s, f           
#  1 -> 2 -> 3 ->1
#       s    f 
#  1 -> 2 -> 3 ->1
#       f    s
#  1 -> 2 -> 3 ->1
#               f,s
#  1 -> 2 -> 3 ->1

tail = ListNode(3)
node = ListNode(2)
head = ListNode(1)

head.next = node
node.next = tail
tail.next = head

s = Solution()
res = s.hasCycle(head)
print(res)

tail.next = None

res = s.hasCycle(head)
print(res)
