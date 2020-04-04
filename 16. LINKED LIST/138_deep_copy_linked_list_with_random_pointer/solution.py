"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:return None
        mapping = {}
        walk = head
        #creating nodes
        while walk:
            mapping[walk] = Node(walk.val, None, None)
            walk = walk.next
        
        walk = head
        #second walk-through, just to assign values to newly created nodes
        while walk:
            if walk.next:
                mapping[walk].next = mapping[walk.next]
            if walk.random:
                mapping[walk].random = mapping[walk.random]
            walk = walk.next
        return mapping[head]