# # Definition for singly-linked list in LinkedListUtils

from LinkedListUtils import ListNode, LinkedListSetup



class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        # count nodes in a linked list 
        walk = head
        counter = 0
        while walk: 
            counter += 1
            walk = walk.next
        width, remainder = divmod(counter, k)
        
        # prev is like dummy head
        prev, walk = None, head
        res = [None for _ in range(k)]
        for i in range(k):
            res[i] = walk
            for _ in range(width + ( 1 if remainder >0 else 0)):
                prev = walk
                walk = walk.next
            if prev:
                prev.next = None
            remainder -= 1
        
        return res



        

setup = LinkedListSetup()
nums = [1, 2, 3, 4, 5, 6, 7, 8]
head = setup.formSinglyLinkedList(nums)
# setup.printLinkedList(head)

s = Solution()
res = s.splitListToParts(head, 4)
for n in range(len(res)):
    setup.printLinkedList(res[n])
    print('')









