"""
Reverse a singly linked list.
Hint:
A linked list can be reversed either iteratively or recursively. 
Could you implement both?
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, next):
        self.val = x
        self.next = next

# Iterative method
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #head                                       res = None
        # 1    ->   2    ->   3   ->   4 -> None
        
        #head     next_node
        # 1    ->   2    ->   3   ->   4 -> None
        
        #head/res next_node
#None <-  1    ->   2    ->   3   ->   4 -> None
        #res    head/next_node
#None <-  1    ->   2    ->   3   ->   4 -> None
        # THE END OF FIRST WHILE LOOP
        
        # res      head    next_node
#None <-  1    ->   2    ->   3   ->   4 -> None
        # res      head    next_node
#None <-  1    <-   2    ->   3   ->   4 -> None
        #        res/head  next_node
#None <-  1    <-   2    ->   3   ->   4 -> None
        #          res    head/next_node
#None <-  1    <-   2    ->   3   ->   4 -> None
        #          res       head   next_node
#None <-  1    <-   2    ->   3   ->   4 -> None
        #          res       head   next_node
#None <-  1    <-   2    <-   3   ->   4 -> None
        #                  res/head next_node
#None <-  1    <-   2    <-   3   ->   4 -> None
        #                    res    head/next_node
#None <-  1    <-   2    <-   3   ->   4 -> None
#.........finally head will be moved to None; while loop stops. 

        res = None
        while head is not None:
            next_node = head.next
            # First node encountered
            # this if condition is executed only once. 
            if res is None:
                res = head
                res.next = None #connect the last node to None
            else:
                # this line is to change direction of linkage of current head 
                head.next = res 
                res = head
            head = next_node
        return res

# test   stunog
node6 = ListNode('g', None)
node5 = ListNode('0', node6)
node4 = ListNode('n', node5)
node3 = ListNode('u', node4)
node2 = ListNode('t', node3)
head = ListNode('5', node2)

def display(headNode):
    while headNode != None:
        print(headNode.val)
        headNode = headNode.next
print("original singly linked list:")
display(head)
s = Solution()
newHead = s.reverseList(head)
print("singly linked list after reversal:")
display(newHead)

