# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        delStart, delEnd, walk = list1, list1, list2
        currentIndex = 0
        #pass all nodes before index a in list1
        while currentIndex != a-1:
            delStart = delStart.next
            delEnd = delEnd.next
            currentIndex += 1
        #pass all nodes between a and b+1, and stay at b.
        while currentIndex != b:
            delEnd = delEnd.next
            currentIndex += 1
        #connect index a in list1 to list2
        delStart.next = walk
        #walk through all nodes in list2
        while walk.next:
            walk = walk.next
        #connect the last node in list2 to list1 starting at index b+1
        walk.next = delEnd.next
        #set the end of removal part to None
        delEnd.next = None
        return list1
        
        