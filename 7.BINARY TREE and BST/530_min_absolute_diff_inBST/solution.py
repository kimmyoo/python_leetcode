"""
Given a binary search tree with non-negative values, 
find the minimum absolute difference between values of any two nodes.

Hint: the minimum absolute difference exists between 2 consecutive elements 
in an ascending array transformed from a BST.
In-order traversal will traverse the tree in ascending manner;
will also need two variables to remember 
the current minimum difference and the previously visited node
"""
import sys
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.curMin = sys.maxsize
        self.pre = None
        
    def inOrder(self, node):
        if node.left:
            self.inOrder(node.left)
        
        if self.pre != None:
            self.curMin = min ((node.val - self.pre), self.curMin)
        #first node which is node with least value (left corner)in BST is encountered
        self.pre = node.val
        
        if node.right:
            self.inOrder(node.right)
        
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        print(self.curMin)
        self.inOrder(root)
        return self.curMin



