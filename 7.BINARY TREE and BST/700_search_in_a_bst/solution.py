# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        # if not root:
        #     return None
        # if root.val == val:
        #     return root
        if not root or root.val == val:
            return root
        if val < root.val:
            # must return the node!!!!the basis case returned a node, 
            # so must the recursive steps
            return self.searchBST(root.left, val)
        if val > root.val:
            return self.searchBST(root.right, val)