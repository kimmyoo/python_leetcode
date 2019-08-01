# Definition for a binary tree node.
"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of 
the two subtrees of every node never differ by more than 1.
Example:
Given the sorted array: [-10,-3,0,5,9],
One possible answer is: [0,-3,9,-10,null,5], 
which represents the following height balanced BST
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.keySet = set()
        
    def dfsToSet(self, node):
        if node:
            self.keySet.add(node.val)
            if node.left:
                self.dfsToSet(node.left)
            if node.right:
                self.dfsToSet(node.right)
    
    def dfsUpdate(self, node):
        if node:
            copyVal = node.val
            greatSum = node.val
            for ele in self.keySet:
                if ele > node.val:
                    greatSum += ele
            node.val = greatSum
            if node.left:
                self.dfsUpdate(node.left)
            if node.right:
                self.dfsUpdate(node.right)
          
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.dfsToSet(root)
        self.dfsUpdate(root)
        print(self.keySet)

#test
n1 = TreeNode(5)
n2 = TreeNode(2)
n3 = TreeNode(13)

n1.left = n2
n1.right = n3

s = Solution()
s.convertBST(n1)

print(n1.val, n2.val, n3.val)



