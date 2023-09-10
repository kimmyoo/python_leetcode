# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root)
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def inorder(root, container):
            if root:        
                inorder(root.left, container)
                container.append(root.val)
                inorder(root.right, container)
            return container
        
        res = []

        return inorder(root, res)
