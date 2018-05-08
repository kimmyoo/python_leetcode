"""
Merge two sorted linked lists and return it as a new list. The new list should
be made by splicing together the nodes of the first two lists.
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, next):
        self.val = x
        self.next = next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0, None) #Dummy node
        # dummy and dummy end refer to the same node
        walk = dummy
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                walk.next = l1
                l1 = l1.next
            else:
                walk.next = l2
                l2 = l2.next
            walk = walk.next
        # if has not reached to end of l1 yet, continue from l1;
        if l1 is not None:
            walk.next = l1
        else:  # if has not reached to end of l2 yet, continue from l2;
            walk.next = l2
        return dummy.next
# test goes here
# sorted listA
NodeD = ListNode('s', None)
NodeC = ListNode('r', NodeD)
NodeB = ListNode('o', NodeC)
NodeA = ListNode('e', NodeB)
listA = NodeA
# sorted listB
NodeH = ListNode('w', None)
NodeG = ListNode('r', NodeH)
NodeF = ListNode('i', NodeG)
NodeE = ListNode('a', NodeF)
listB = NodeE
s = Solution()
mergedList = s.mergeTwoLists(listA, listB)
while mergedList != None:
    print (mergedList.val)
    mergedList = mergedList.next


