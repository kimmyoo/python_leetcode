"""
Given a Binary Search Tree (BST), 
convert it to a Greater Tree such that 
every key of the original BST is changed to 
the original key plus sum of all keys greater than the original key in BST.
     5                  18
    / \      ->        /  \
   2   13            20    13
"""
#my submission: last test failed for exceeding time limit.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1(object):
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

class Solution2(object):
    def __init__(self):
        self.sum = 0
    
    def reverseInOrderTraversal(self, node):
        if node:
            if node.right:
                self.reverseInOrderTraversal(node.right)
            self.sum += node.val
            node.val = self.sum
            if node.left:
                self.reverseInOrderTraversal(node.left)
    
    def convertBST(self,root):
        self.reverseInOrderTraversal(root)
        return root
                
    
#test
n1 = TreeNode(5)
n2 = TreeNode(2)
n3 = TreeNode(13)

n1.left = n2
n1.right = n3

#s = Solution1()
#s.convertBST(n1)

s2 = Solution2()
s2.convertBST(n1)

print(n1.val, n2.val, n3.val)