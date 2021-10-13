# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.modeCount = {}
        
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        self.dfs(root)
        maxCount = max(self.modeCount.values())
        print(maxCount)
        res = [k for k, v in self.modeCount.items() if v == maxCount]
        return res

    def dfs(self, node):
        if node:
            if node.val not in self.modeCount:
                self.modeCount[node.val] = 1
            else:
                self.modeCount[node.val] += 1
        if node.left:
            self.dfs(node.left)
        if node.right:
            self.dfs(node.right)