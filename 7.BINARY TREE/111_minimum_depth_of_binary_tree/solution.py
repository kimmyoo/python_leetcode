# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if root.left and root.right:
            left = self.minDepth(root.left)
            right = self.minDepth(root.right)
            return min(left, right) + 1
        #this is different than the max depth of binary Tree
        if not root.left or not root.right:
            return max(self.minDepth(root.right), self.minDepth(root.left))+ 1