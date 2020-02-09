# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    #refer to Leetcode #142
    def getCycleEntry(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                while head != slow:
                    head = head.next
                    slow = slow.next
                return head
        return None

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        count = 0
        walkA, walkB = headA, headA
        
        while walkA.next:
            walkA = walkA.next
            count +=1
        #after hitting the end, 
        #connect the end to headB to form a cycle
        walkA.next = headB
        #then we find the starting point of the cycle
        intersect = self.getCycleEntry(headA)
        #however, you are not allowed to change either list, 
        #so we do need to reconnect the end shared by both lists
        #back to None before returning intersected node.
        while count > 0:
            walkB = walkB.next
            count -= 1
        walkB.next = None
        
        return intersect
    