# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxLength = 0
        def depth(node):
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            self.maxLength = max (left + right + 1, self.maxLength)
            return max(left, right)+1
        
        depth(root)
        if self.maxLength == 0:
            return 0
        else:
            return self.maxLength - 1

