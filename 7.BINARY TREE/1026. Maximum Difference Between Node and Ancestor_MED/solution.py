# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxAncestorDiffBottomUp(self, root):
        """
        :type root: TreeNode
        :rtype: int
        my own solution: bottom up approach
        """
        self.res = 0
        
        def dfs(root):
            if root:
                #no right subtree
                if root.left and not root.right:
                    left = dfs(root.left)
                    minMaxTuple = ( min(left[0], root.val), max(left[1], root.val))
                #no left subtree
                if root.right and not root.left:
                    right = dfs(root.right)
                    minMaxTuple = ( min(right[0], root.val), max(right[1], root.val))
                # have both left and right subtrees
                if root.left and root.right:
                    left = dfs(root.left)
                    right = dfs(root.right)
                    minMaxTuple = (min(left[0], right[0], root.val), max(left[1], right[1], root.val))
                # current node is leaf node
                if not root.left and not root.right:
                    minMaxTuple = (root.val, root.val)
                self.res = max(self.res, max(abs(root.val-minMaxTuple[0]), abs(root.val-minMaxTuple[1])))
                #print(self.res)
                return minMaxTuple

        dfs(root)
        return self.res
    

    def maxAncestorDiffTopDown(self, root):
        def helper(root, mn, mx):
            if not root:
                return mx-mn
            mn = min(root.val, mn)
            mx = max(root.val, mx)
            left = helper(root.left, mn, mx)
            right = helper(root.right, mn, mx)
            return max(left, right)