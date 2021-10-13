# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def inorderTraversal(self, root, res):
        if root:
            self.inorderTraversal(root.left, res)
            res.append(root)
            self.inorderTraversal(root.right, res)
            
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        container = []
        # inorder traversal collects all nodes in container
        self.inorderTraversal(root, container)

        first, second = None, None
        for i in range(len(container)-1):
            if container[i].val > container[i+1].val and not first:
                first = container[i]
            if container[i].val > container[i+1].val and first:
                second = container[i+1]
        first.val, second.val = second.val, first.val
            