# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# my own solution
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.ans = []
        res = ""
        
        def dfs(node, res):
            if not node:
                return
            else:
                res += str(node.val) + '->'
            if node.left:
                dfs(node.left, res)
            if node.right:
                dfs(node.right, res)
            #if we reach to a leaf node
            if not node.left and not node.right:
                self.ans.append(res[:-2])

        dfs(root, res)
        return self.ans
