"""
Given the root node of a binary search tree (BST) and a value. 
You need to find the node in the BST that the node's value equals 
the given value. Return the subtree rooted with that node. 
If such node doesn't exist, you should return NULL.

For example, 
Given the tree:
        4
       / \
      2   7
     / \
    1   3

And the value to search: 2
You should return this subtree:
      2     
     / \   
    1   3
In the example above, if we want to search the value 5, since there is 
no node with value 5, we should return NULL.
Note that an empty tree is represented by NULL, therefore you would 
see the expected output (serialized tree format) as [], not null.
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def searchBST(self, root, val):
        #~ :type root: TreeNode
        #~ :type val: int
        #~ :rtype: TreeNode
        while root:
            if root.val == val:
                return root
            elif val < root.val:
                root = root.left
            else:
                root = root.right

    def preorderTraversal(self, root):
        """
        type root: TreeNode
        rtype: list
        """
        res = []
        if root:
            res.append(root.val)
            res.extend(self.preorderTraversal(root.left))
            res.extend(self.preorderTraversal(root.right))
        return res

    def inorderTraveral(self, root):
        res = []
        if root.left:
            res = res + self.inorderTraveral(root.left)
        res.append(root.val)
        if root.right:
            res = res + self.inorderTraveral(root.right)
        return res
    
    def postorderTraveral(self, root):
        res = []
        if root.left:
            res = res + self.postorderTraveral(root.left)
        if root.right:
            res = res + self.postorderTraveral(root.right)
        res.append(root.val)
        return res
    
    def arrToBst(self, A):
        """
        type A: list
        rtype: TreeNode
        """
        if not A:
            return None
        A.sort()
        arr_size = len(A)
        mid = arr_size//2
        root = TreeNode(A[mid])
        root.left = self.arrToBst(A[:mid])
        root.right = self.arrToBst(A[mid+1:])
        return root
    
    def trimBST(self, root, L, R):
        """
        type root: TreeNode
        type L, R: int; L and R are left and right key boundaries
        rtype: TreeNode
        """
        def trim(root):
            if not root:
                return None
            # If the value of this node is greater than R, then the 
            # whole right subtree will be greater
            # so we can discard the right sub tree and return the root 
            # of the trimmed left sub tree
            elif root.val > R:
                return trim(root.left)
            # If the value of this node is less than L, then the whole 
            # left subtree will be smaller, 
            # so we can discard the left sub tree and return the root 
            # of the trimmed right sub tree 
            elif root.val < L:
                return trim(root.right)
            # If the value of this node does not need to be trimmed
            # we need to pass this recursive call downwards to both sides
            root.left = trim(root.left)
            root.right = trim(root.right)
            return root
        return trim(root)

#test code
s = Solution()
A = [i for i in range(10)]
tree = s.arrToBst(A)
res = s.searchBST(tree, 25)
print("trying ot find 25:", res)
preorderTr = s.preorderTraversal(tree)
inorderTr = s.inorderTraveral(tree)
postorderTr = s.postorderTraveral(tree)
trimmedTree = s.trimBST(tree, 2, 8)
print("pre-order:", preorderTr)
print("in-order:", inorderTr)
print("post-order:", postorderTr)
print("trimmed tree is:", s.inorderTraveral(trimmedTree), "root:", trimmedTree.val)
