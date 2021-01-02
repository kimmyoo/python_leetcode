# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = self.levelTraversal(root)
        print("hello")
        return res
        
    def levelTraversal(self, root):
        if not root:
            return []
        dq = deque()
        dq.append(root)
        res = []
        
        while dq:
            i = 0
            l = len(dq)
            levelRes = []
            while i < l:
                curNode = dq.popleft()
                levelRes.append(curNode.val)
                if curNode.left:
                    dq.append(curNode.left)
                if curNode.right:
                    dq.append(curNode.right)
                i+=1
            res.append(levelRes[-1])
        return res