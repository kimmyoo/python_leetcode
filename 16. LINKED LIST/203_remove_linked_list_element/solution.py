"""
Remove all elements from a linked list of integers that have value val.
Example:
Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return None
        
        cur, nxt = head, head
        
        #this while deals with nodes beginning at the head whose values
        #are equal to val
        while cur and cur.val == val:
            cur = cur.next
            nxt = nxt.next
        head = cur
        
        if not head: # remember to check head
            return None
        #create a new node object pointing to 
        #the node after head: shift one position
        nxt = head.next
        
        while cur.next:
            #this while deals with two adjacent nodes whoses values are 
            #not equal to val
            while nxt and cur.val != val and nxt.val != val:
                cur = cur.next
                nxt = nxt.next
            #this while deals with node(s) whose val is equal to val
            while nxt and nxt.val == val:
                nxt = nxt.next
            #this line reconnects the list excluding nodes whose values
            #are equal to val
            cur.next = nxt
        return head
            