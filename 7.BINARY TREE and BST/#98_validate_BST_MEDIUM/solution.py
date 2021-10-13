# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from __builtin__ import False

class Solution(object):
    def isValidBST_A(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.dfs(root, float('-inf'), float("inf"))

    
    def isValidBST_B(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack, pre = [], float('-inf')
        while stack or root:
            #inner while is responsible for moving to the left most of current root
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= pre:
                return False
            pre = root.val
            root = root.right
        return True

    def dfs(self, node, lower, upper):
        if not node:
            return True
        if node.val >= upper or node.val <= lower:
            return False
        if not self.dfs(node.left, lower, node.val):
            return False
        if not self.dfs(node.right, node.val, upper):
            return False
        return True