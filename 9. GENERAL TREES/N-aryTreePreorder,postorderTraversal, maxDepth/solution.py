
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children




class Solution(object):
    def preorderConstruct(self, A, k):
        """
        :type A: list
        :type k: int
        :rtype: Node
        """
        pass
    
    def preorderTraversal(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        res.append(root.val)
        for child in root.children:
            #res = res + self.preorder(child)
            res.extend(self.preorderTraversal(child))
        return res

    def postorderTraversal(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        for child in root.children:
            res.extend(self.postorderTraversal(child))
        res.append(root.val)
        return res

    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root is None:
            return 0
        maxDepth = 0
        for ch in root.children:
            maxDepth = max(maxDepth, self.maxDepth(ch))
        return 1 + maxDepth
