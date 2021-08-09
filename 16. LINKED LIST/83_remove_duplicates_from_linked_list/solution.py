"""
Given a sorted linked list, 
elete all duplicates such that each element appear only once.

Example 1:
Input: 1->1->2->3->3
Output: 1->2->3
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        curNode, nxtNode = head, head
        while nxtNode:
            #while nextNode is to make sure we don't go all the way to
            #the end (None)
            while nxtNode and curNode.val == nxtNode.val:
                nxtNode = nxtNode.next
            curNode.next = nxtNode
            curNode = nxtNode
        return head

    def deleteDuplicatesB(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        cur = head
        
        while cur and cur.next:
            first = cur
            second = cur.next
            
            while first.val == second.val:
                second = second.next
                if not second:
                    break

            first.next = second
            cur = cur.next
        return head