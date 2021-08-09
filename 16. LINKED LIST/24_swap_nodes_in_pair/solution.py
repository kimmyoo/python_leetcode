# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode()      
        dummy.next = head
        cur = dummy
        
        while cur.next and cur.next.next:
            first = cur.next
            second = cur.next.next
            
            first.next = second.next
            cur.next = second
            second.next = first
            
            cur = cur.next.next
        
        return dummy.next