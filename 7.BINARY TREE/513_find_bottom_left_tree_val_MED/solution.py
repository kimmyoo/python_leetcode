# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.levelOrder(root)
        
    def levelOrder(self, root):
        st = deque()
        st.append(root)
        leftMost = root
        while st:
            i = 0
            l = len(st)
            while i < l:
                curNode = st.popleft()
#                 if curNode.left:
#                     st.append(curNode.left)
#                 if curNode.right:
#                     st.append(curNode.right)
                st += filter(None, (curNode.left, curNode.right))
                i+=1
            #in case the last time the st is empty
            if st:
                leftMost = st[0]
        return leftMost.val