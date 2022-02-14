# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):
    def flattenRight(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        
        """
        巧用stack的先进后出的性质
        给curNode的右节点 连接到左节点上 但左节点任然保留在stack上
        """
        if not root:
            return
        
        stack = deque()
        stack.append(root)
        while stack:
            curNode = stack.pop()
            if curNode.right: stack.append(curNode.right)
            if curNode.left: stack.append(curNode.left)
            # when using a stack always check if it's empty
            if stack:
                curNode.right = stack[-1]
            curNode.left = None
    
    def flattenLeft(self, root):
        if not root:
            return
        stack = deque()
        stack.append(root)
        while stack:
            curNode = stack.pop()
            if curNode.left: stack.append(curNode.left)
            if curNode.right: stack.append(curNode.right)
            if stack:
                curNode.left = stack[-1]
            curNode.right = None
