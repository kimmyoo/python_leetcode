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
    arr = []
    def preOrderSerialize(self, node):
        if node:
            self.arr.append(node.val)
            self.preOrderSerialize(node.left)
            self.preOrderSerialize(node.right)

    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root:
            if root.val == val:
                self.preOrderSerialize(root)
            elif val < root.val:
                self.searchBST(root.left, val)
            else:
                self.searchBST(root.right, val)
        return self.arr

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

#test code
s = Solution()
A = [i for i in range(100)]
tree = s.arrToBst(A)
res = s.searchBST(tree, 25)
print(res)


"""
    #leetcode solution
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

"""
