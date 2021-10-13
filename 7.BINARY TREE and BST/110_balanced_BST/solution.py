# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# method 1: brutal force, getHeight O(n), isBalanced (log(n)), the overall time complexity is nlogn
class Solution1(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # base case: when the root't parent is a leaf node, return True
        if not root:
            return True
        left = self.getHeight(root.left)
        right = self.getHeight(root.right)
        if abs(left-right) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def getHeight(self, node):
        #think of depth from bottom to top
        # if not node, it means the node's parent is a leaf node
        if not node:
            return 0
        left = self.getHeight(node.left)
        right = self.getHeight(node.right)
        #for leaf nodes, left and right is equal to 0, and the height of current node is 1
        return max(left, right) + 1

#method 2: method 1 has many useless checking to see if subtrees are balance or not. 
# we can simply use a global variable self.isBalanced to see if any of the substrees is unbalanced. 
# if any of the subtree is unbalanced, we update self.isBalanced when getting the height of each node 
# and we simply return this variable afterwards. 
class Solution2(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.isBalanced = True
        self.getHeight(root)
        return self.isBalanced

    def getHeight(self, node):
        #think of depth from bottom to top
        # if not node, it means the node's parent is a leaf node
        if not node:
            return 0
        left = self.getHeight(node.left)
        right = self.getHeight(node.right)
        #update isBalanced when we get height of each node
        #no need to go through level by level to see if the tree is balanced.
        if abs(left - right) > 1:
            self.isBalanced = False
        return max(left, right) + 1

