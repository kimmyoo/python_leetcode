# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
Given a binary tree, return the sum of values of nodes with even-valued grandparent.  
(A grandparent of a node is the parent of its parent, if it exists.)
If there are no nodes with an even-valued grandparent, return 0.
"""
class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0

        #pass parent and grandparent to each recursive call
        def dfs(node, parent, grandpa):
            if not node:
                return
            if grandpa and grandpa.val % 2 == 0:
                self.res += node.val
            if node.left:
                dfs(node.left, node, parent)
            if node.right:
                dfs(node.right, node, parent)
        
        dfs(root, None, None)
        return self.res