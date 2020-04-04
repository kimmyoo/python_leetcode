"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur1 = l1
        cur2 = l2
        carry = 0
        dummyHead = ListNode(0)
        walk = dummyHead
        while cur1 or cur2 or carry:
            s = 0
            if cur1:
                s+=cur1.val
                cur1 = cur1.next
            if cur2:
                s+=cur2.val
                cur2 = cur2.next
            s+=carry
            carry = s/10
            if carry:
                s -=10
            walk.next = ListNode(s)
            walk = walk.next
        return dummyHead.next