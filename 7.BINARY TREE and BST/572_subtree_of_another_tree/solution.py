# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# TRY IMPLEMENT THIS IN THIS WAY:
# CONVERT THE TREE INTO A STRING AND CHECK IF THE t is a substring of s string.
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not t:
            return True
        return self.dfs(s, t)
          
    def sameTree(self, node1, node2):
        if not node1 and not node2:
            return True
        elif node1 and node2 and node1.val == node2.val:
            print(node1.val)
            return self.sameTree(node1.left, node2.left) and self.sameTree(node1.right, node2.right)
        else:
            return False

    def dfs(self, s, t):
        if not s:
            return False
        if self.sameTree(s, t):
            return True
        return self.dfs(s.left, t) or self.dfs(s.right, t)#"or"