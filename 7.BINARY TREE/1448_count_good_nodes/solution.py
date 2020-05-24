# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        my own solution: pass curMax value down to the subtrees if current is good node, ie curcount += 1
        and update curMax
        """
        def dfs(root, curMax):
            if not root:
                return 0
            if root.val >= curMax:
                cur = 1
                curMax = max(curMax, root.val)
            else:
                cur = 0
            return cur + dfs(root.left, curMax) + dfs(root.right, curMax)
            
        res = dfs(root, root.val)
        return res

    def goodNodes2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.count = 0
        
        def dfs(root, curMax):
            if not root:
                return
            if root.val >= curMax:
                self.count += 1
                curMax = max(curMax, root.val)
            dfs(root.left, curMax)
            dfs(root.right, curMax)
            
        dfs(root, root.val)
        return self.count