# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        #base cases:
        if N % 2 == 0: return []
        if N == 1: return [TreeNode(0)]
        res = []
        #allocate 1, 3, 5, 7...i nodes to left
        #accordingly, right will have N-i-1 nodes
        #simply create root node for that pair of left and right and append root to res
        for i in range(1, N, 2):
            # l will be a left node returned by recursive call
            for l in self.allPossibleFBT(i):
                for r in self.allPossibleFBT(N-i-1):
                    root = TreeNode(0)
                    root.left = l
                    root.right = r
                    res.append(root)
        return res