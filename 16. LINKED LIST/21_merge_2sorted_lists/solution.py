"""
Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists.
Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""
class Solution(object):
    def mergeTwoLists1(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        if not l1 and not l2:
            return None
        
        walk1, walk2 = l1, l2
        #this block can be rewritten to method2
        if l1.val <= l2.val:
            newHead = l1
            walk1 = walk1.next
        else:
            newHead = l2
            walk2 = walk2.next
        
        walk = newHead
        
        while walk1 and walk2:
            if walk1.val <= walk2.val:
                walk.next = walk1
                walk1 = walk1.next
            else:
                walk.next = walk2
                walk2 = walk2.next
            walk = walk.next
        
        walk.next = walk1 if walk1 else walk2
        return newHead
    
    def mergeTwoLists2(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        if not l1 and not l2:
            return None
        #don't return this dummy node
        #return dummyHead's next node as the real head after merging
        dummyHead = ListNode(None)
        walk = dummyHead
        while l1 and l2:
            if l1.val <= l2.val:
                walk.next = l1
                l1 = l1.next
            else:
                walk.next = l2
                l2 = l2.next
            walk = walk.next
        #after the while loop, link the remaining nodes in either l1 or l2
        walk.next = l1 if l1 else l2
        return dummyHead.next

