# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    #  time: O(n)  space: O(1)
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return None

        # two dummy nodes
        lHead = ListNode(-1)
        rHead = ListNode(-1)
        
        lPointer, rPointer = lHead, rHead

        while head:
            if head.val < x:
                lPointer.next = head
                lPointer = lPointer.next
            else:
                rPointer.next = head
                rPointer = rPointer.next
            head = head.next
        
        lPointer.next = rHead.next
        rPointer.next = None
        return lHead.next

    # time: O(n)  space: O(n)
    def partition2(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        left, right = [], []
        while head:
            if head.val < x:
                left.append(head.val)
            else:
                right.append(head.val)
            head = head.next
        
        if len(right):
            rightHead = ListNode(right.pop(0))
            rPtr = rightHead
            while (len(right) > 0):
                nRightNode = ListNode(right.pop(0))
                rPtr.next = nRightNode
                rPtr = rPtr.next
        else:
            rightHead = None

        if len(left):
            leftHead = ListNode(left.pop(0))
            lPtr = leftHead
            while (len(left)):
                nLeftNode = ListNode(left.pop(0))
                lPtr.next = nLeftNode
                lPtr = lPtr.next
            lPtr.next = rightHead
        else:
            return rightHead
        
        return leftHead