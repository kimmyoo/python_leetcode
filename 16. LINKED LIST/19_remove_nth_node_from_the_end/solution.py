# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd1(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        #two passes, 1 pointer, try using two pointers one pass to implement
        if head:
            count, walk = 1, head
            while walk.next:
                walk = walk.next
                count+=1
        else:
            return None
        
        dummy = ListNode(0)
        dummy.next = head
        walk, i = dummy, 0

        while walk:
            #if we reach the node that is right before the target node
            if i == count - n:
                walk.next = walk.next.next
            walk = walk.next
            i+=1
        return dummy.next