"""
Given a tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only 1 right child.

Example 1:
Input: [5,3,6,2,4,null,8,1,null,null,null,7,9]

       5
      / \
    3    6
   / \    \
  2   4    8
 /        / \ 
1        7   9

Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

 1
  \
   2
    \
     3
      \
       4
        \
         5
          \
           6
            \
             7
              \
               8
                \
                 9  
Note:

The number of nodes in the given tree will be between 1 and 100.
Each node will have a unique integer value from 0 to 1000.
"""



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        A = []
        self.inOrderTraversalToArray(root, A)
        root = self.arrayToBst(A)
        return root
    
    
    def inOrderTraversalToArray(self, root, A):
        """
        in order traversal to add elements to List A
        type A: TreeNode, List
        """
        if not root:
            return
        if root.left:
            self.inOrderTraversalToArray(root.left, A)
        A.append(root.val)
        if root.right:
            self.inOrderTraversalToArray(root.right, A)
        
    def arrayToBst(self, A):
        """
        type A: List
        rtype: TreeNode
        """
        root = TreeNode(A.pop(0))
        while len(A) > 0:
            root.right = self.arrayToBst(A)
        return root


#leetcode solution #2
#~ class Solution:
    #~ def increasingBST(self, root):
        #~ def inorder(node):
            #~ if node:
                #~ inorder(node.left)
                #~ node.left = None
                #~ self.cur.right = node
                #~ self.cur = node
                #~ inorder(node.right)

        #~ ans = self.cur = TreeNode(None)
        #~ inorder(root)
        #~ return ans.right
