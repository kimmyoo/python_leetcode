# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sumTilt = 0
        
        def depthSearch(node):
            if not node:
                return 0
            lSum = depthSearch(node.left)
            rSum = depthSearch(node.right)
            tilt = abs(lSum-rSum)
            #update sumTilt while getting the sum of l and r and node.val recursively
            self.sumTilt += tilt
            return lSum + rSum + node.val
        
        depthSearch(root)
        return self.sumTilt


