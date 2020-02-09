# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        curOdd = head
        curEven = head.next
        evenHead = curEven
        
        #this while loop condition ensures that
        #there are at least 3 nodes
        #also we check curEven and curEven.next because
        #curEven and curEven.next will hit the end of the link list FIRST!
        while curEven and curEven.next:
            curOdd.next = curEven.next
            curOdd = curOdd.next
            curEven.next = curOdd.next
            curEven = curEven.next
        
        curOdd.next = evenHead
        return head