"""
Given the root node of a binary search tree, 
return the sum of values of all nodes with value between L and R (inclusive).
The binary search tree is guaranteed to have unique values.

Example 1:
Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32
"""
import TreeNode

class Solution(object):
    def __init__(self):
        self.rangeSum = 0
    
    def inOrderTraversal(self, root, L, R):
        if root:
            # don't go through the left subtree if root.val < L
            if root.val > L:
                self.inOrderTraversal(root.left, L, R)
            if L <= root.val <= R:
                self.rangeSum += root.val
            if root.val < R:
                self.inOrderTraversal(root.right, L, R)    
    
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        self.inOrderTraversal(root, L, R)
        return self.rangeSum
        
