# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.max = 0
        self.cnt = 0
        self.pre = None
        self.res = []

    def inOrderTraversal(self, node):
        if node.left:
            self.inOrderTraversal(node.left)
        
        if node:
            if self.pre != node.val:
                self.cnt = 1
                self.pre = node.val
            else:
                self.cnt+=1
            #here must be if...elif conditional. why? because it's a bifurcation!
            #because the first if condition will make self.cnt equal to self.max, 
            #if it's followed by another if 
            #node.val will be added twice, which is incorrect
            if self.cnt > self.max:
                self.max = self.cnt
                self.res = [node.val]
            elif self.cnt == self.max:
                self.res.append(node.val)
                
        if node.right:
            self.inOrderTraversal(node.right)

    
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        self.inOrderTraversal(root)
        #print(self.max, self.cnt)
        return self.res
    