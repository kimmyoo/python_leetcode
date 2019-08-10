# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.sum = 0
    
    def dfs (self, node):
        if node:
            #if left exists and it's a leaf node
            if node.left and self.isLeaf(node.left):
                self.sum += node.left.val
            else:
                self.dfs(node.left)
            if node.right:
                self.dfs(node.right)

    def isLeaf(self, node):
        if node:
            if not node.left and not node.right:
                return True
            else:
                return False

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dfs(root)
        return self.sum


