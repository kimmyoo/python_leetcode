"""
Consider all the leaves of a binary tree.  From left to right order, 
the values of those leaves form a leaf value sequence.


"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def dfs(root, A):
            if root:
                if not root.left and not root.right:
                    A.append(root.val)
                dfs(root.left, A)
                dfs(root.right, A)
        A = []
        B = []
        dfs(root1, A)
        dfs(root2, B)
        return A == B