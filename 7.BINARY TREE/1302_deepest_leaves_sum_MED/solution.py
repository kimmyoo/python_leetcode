# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sum = 0
        s = [root]
        
        while s:
            l = len(s)
            curLevelSum = 0
            for i in range(l):
                curNode = s.pop(0)
                curLevelSum += curNode.val
                if curNode.left:
                    s.append(curNode.left)
                if curNode.right:
                    s.append(curNode.right)
        return curLevelSum
    
    def deepestLeavesSumB(self, root):
        """
        大神写法
        pre are nodes in the previous level.
        q are node in the current level.
        When current level are empty,
        the previous level are the deepest leaves.
        """
        q = [root]
        while q:
            pre, q = q, [child for p in q for child in [p.left, p.right] if child]
        return sum(node.val for node in pre)
    