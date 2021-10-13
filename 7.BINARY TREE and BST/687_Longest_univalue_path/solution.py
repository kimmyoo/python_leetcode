# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        def extensionLength(node):
            if not node:
                return 0
            leftExt = extensionLength(node.left)
            rightExt = extensionLength(node.right)
            l = r = 0
            if node.left and node.left.val == node.val:
                l = leftExt + 1
            if node.right and node.right.val == node.val:
                r = rightExt + 1
            self.res = max(self.res, l + r)
            return max(l, r)
        extensionLength(root)
        return self.res