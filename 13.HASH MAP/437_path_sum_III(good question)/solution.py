# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # double recursive solution exceeds time limit
    def __init__(self):
        self.numOfPath = 0

    def dfs (self, root, sum):
        #edge case or defensive condition
        if not root:
            return
        #process
        if sum == root.val:
            self.numOfPath += 1
            #print("Ended at:", root.val)
        sum -= root.val
        #recursive cases
        self.dfs(root.left, sum)
        self.dfs(root.right, sum)

    def pathSum(self, root, sum):
        if not root:
            return 0
        self.dfs(root, sum)
        self.pathSum(root.left, sum)
        self.pathSum(root.right, sum)
        return self.numOfPath