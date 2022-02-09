# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.helper(1, n)
    
    
    def helper(self, start, end):
        # edges cases for each ending number
        if start > end:
            return [None]
        
        # container to hold the root nodes
        allTrees = []
        for curVal in range(start, end+1):
            # get all the left subtrees and right subtrees
            allLeftTrees = self.helper(start, curVal-1)
            allRightTrees = self.helper(curVal+1, end)
            
            # using for loop to find all possible combinations
            for lTree in allLeftTrees:
                for rTree in allRightTrees:
                    curRoot = TreeNode(curVal)
                    curRoot.left = lTree
                    curRoot.right = rTree
                    allTrees.append(curRoot)
        return allTrees