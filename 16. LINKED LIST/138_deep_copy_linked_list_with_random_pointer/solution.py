# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:return None
        mapping = {}
        walk = head
        # creating nodes and save them in mapping
        # both pointers points to None now
        while walk:
            mapping[walk] = Node(walk.val, None, None)
            walk = walk.next
        walk = head

        #second walk-through, just to assign values to newly created nodes
        while walk:
            # dict.get() returns None if a valid key is provided.
            mapping[walk].next = mapping.get(walk.next)
            mapping[walk].random = mapping.get(walk.random)
            walk = walk.next
        # new head is the value saved in mapping, key is head
        return mapping[head]