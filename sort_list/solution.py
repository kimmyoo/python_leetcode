"""
Given a unsorted singly linked list, writen a function and return a 
sorted singly linked list
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        if head is None or head.next is None:
            return head

        # Find the middle node
        # e.g.   w - i - n - i - r - a - y
        # 1    s/f/p
        # 2      p   s   f
        # 3          p   s       f
        # 4              p   s           f
        
        #left:   w - i - n 
        #right:  i - r - a - y
        
        #        w - i - n       left list
        #1     s/f/p   
        #2       p   s   f 
        
        #left:   p 
        #right:  s - f
        
        #        i - r - a - y - None     right list 
        #1     s/f/p 
        #2       p   s   f
        #3           p  s/f
        #4               p   s    f 

        #left:   i - r 
        #right:  a - y
        slow = head
        fast = head
        prev = head  # Previous node to slow
        while fast is not None and fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Split into two lists
        left = head
        right = None
        if slow != fast:
            prev.next = None
            right = slow
        left = self.sortList(left)
        right = self.sortList(right)
        return self.merge(left, right)

    def merge(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        res = None
        end = res
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                small = l1
                l1 = l1.next
            else:
                small = l2
                l2 = l2.next
            # First node
            if res is None:
                res = small
                end = res
            else:
                end.next = small
                end = end.next
        if l1 is not None:
            end.next = l1
        if l2 is not None:
            end.next = l2
        return res

# -------test---------
node1 =ListNode('w')
node2 =ListNode('i')
node3 =ListNode('n')
node4 =ListNode('i')
node5 =ListNode('r')
node6 =ListNode('a')
node7 =ListNode('y')

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

s = Solution()
newhead = s.sortList(node1)
walk = newhead
while walk!= None:
    print(walk.val)
    walk = walk.next
    
