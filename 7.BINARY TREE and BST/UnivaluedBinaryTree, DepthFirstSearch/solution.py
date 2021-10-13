"""
A binary tree is univalued if every node in the tree has the same value.
Return true if and only if the given tree is univalued.


Approach:
Let's output all the values of the array. 
After, we can check that they are all equal.
To output all the values of the array, we perform a depth-first search.
depth-first search includes preorder, inorder, and postoder traversals.
"""

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        arr = []
        def preOrderTraversal(node):
            if node:
                arr.append(node.val)
                preOrderTraversal(node.left)
                preOrderTraversal(node.right)
        
        preOrderTraversal(root)
        #this a how you find out if the array contains elements of 
        #the same value
        return len(set(arr)) == 1


    def insertLevelOrder(self, A, root, i, n):
        if i < n:
            #base case:
            tempNode = TreeNode(A[i])
            root = tempNode
            #~ print(root.val)
            #recursively insert to left and right
            root.left = self.insertLevelOrder(A, root.left, 2*i+1, n)
            root.right = self.insertLevelOrder(A, root.right, 2*i+2, n)
            return root


#test code
s = Solution()
testArrayA = [3, 3, 3, 3, 3, 3, 3]
testArrayB = [1, 2, 3, 4, 5]

nodeA = nodeB = None
rootA = s.insertLevelOrder(testArrayA, nodeA, 0, len(testArrayA))
rootB = s.insertLevelOrder(testArrayB, nodeB, 0, len(testArrayB))

resA = s.isUnivalTree(rootA)
resB = s.isUnivalTree(rootB)

print (resA, resB)
