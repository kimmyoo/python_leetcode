# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
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
                dq += filter(None, (curNode.left, curNode.right))
                i+=1
            res.append(max(levelRes))
        return res