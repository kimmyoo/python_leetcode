# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pt1 = pt2 = head
        
        while pt1 is not None:
            if pt1.next is None:
                return pt2
            pt1 = pt1.next.next
            pt2 = pt2.next
        return pt2
