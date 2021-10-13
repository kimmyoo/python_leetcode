# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        #two lists to remember the path from root to given node p and q
        pathA, pathB = [], []
        if self.hasPath(root, p, pathA) and self.hasPath(root, q, pathB):
            l = min(len(pathA), len(pathB))
            for i in range(l):
                if pathA[i].val!= pathB[i].val:
                    return pathA[i-1]
            #this is for an edge case where  two paths are like
            #[3, 5, 6, 7] and [3, 5]
            return pathA[l-1]
    #dfs to find whether there is path from root to a given node, 
    #remember the path at the same time.
    def hasPath(self, root, target, path):
        if not root:
            return False
        path.append(root)
        if root.val == target.val:
            return True
        if self.hasPath(root.left, target, path) or self.hasPath(root.right, target, path):
            return True
        else:
            path.pop(-1)
            return False