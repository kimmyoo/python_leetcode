"""
Given a non-empty binary tree, return the average value 
of the nodes on each level in the form of an array.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        q = [root]
        res = []
        
        while q:
            levelSum = 0.0
            levelCount = 0
            #for loop will loop through all nodes on current level
            for i in range (0, len(q)):
                currentNode = q.pop(0)
                if currentNode:
                    if currentNode.left:
                        q.append(currentNode.left)
                    if currentNode.right:
                        q.append(currentNode.right)
                    levelSum += currentNode.val
                    levelCount += 1
                i+=1
            res.append(levelSum/levelCount)
        return res
                
