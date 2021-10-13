# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from heapq import merge

class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        self.tree1 = []
        self.tree2 = []
        #don't forget edge case: root is None
        if root1:
            self.inOrderTraversal(root1, self.tree1)
        if root2:
            self.inOrderTraversal(root2, self.tree2)
        #to save time, I used merge()
        #知识点：使用built-in functions to perform merging two sorted lists
        res = list(merge(self.tree1, self.tree2))
        return res
    
    #utility function to put node.val into a list
    def inOrderTraversal(self, root, container):
        if root.left:
            self.inOrderTraversal(root.left, container)
        if root:
            container.append(root.val)
        else:
            return
        if root.right:
            self.inOrderTraversal(root.right, container)
 