"""
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:
Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next):
        self.val = x
        self.next = next

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        
        i = 1 
        res = head  # Start of the beginning part
        res_end = head  # End of the beginning part
        rev = None  # Start of reversed part
        rev_end = None  # End of reversed part
        
        #the purpose of this while loop is to check if the current node
        #falls within the range [m, n]
        #if current node is less than m
        walk = head
        while walk is not None:
            next_node = walk.next
            if i < m:
                res_end = walk # update the res_end node to current walk node
            elif i >= m and i <= n:
                walk.next = rev #connect None to the currernt walk node (the beginning of reversed part)
                rev = walk# set the beginning of reversed part to current walk node
                if i == m: #  if current node is very first node in reversed part,
                    rev_end = walk # set the end of the reverse part to walk 
            else:  # i > n
                break
            walk = next_node
            i += 1
        
        
        # 2 senarios: No beginning part or has a beginning part.
        if m == 1:
            res = rev
            res_end = rev_end
        else:
            res_end.next = rev # connect the beginning of reversed part to the end of beginning part
        
        rev_end.next = walk # connect the end of reverse part to current walk node
        return res
# test 
tail = ListNode(0, None)
node3 = ListNode(1, tail)
node2 = ListNode(2, node3)
node1 = ListNode(3, node2)
head = ListNode(4, node1)

def display(head_node):
    while head_node is not None:
        print (head_node.val)
        head_node = head_node.next

display(head)
s = Solution()
s.reverseBetween(head, 2, 3)
print("after reversing:")
display(head)


