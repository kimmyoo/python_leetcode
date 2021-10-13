# Definition for a binary tree node.
"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of 
the two subtrees of every node never differ by more than 1.
Example:
Given the sorted array: [-10,-3,0,5,9],
One possible answer is: [0,-3,9,-10,null,5], 
which represents the following height balanced BST

For a sorted array, the left half will be in the left subtree, 
middle value as the root, right half in the right subtree. This holds true for every node:

[1, 2, 3, 4, 5, 6, 7] -> left: [1, 2, 3], root: 4, right: [5, 6, 7]
[1, 2, 3] -> left: [1], root: 2, right: [3]
[5, 6, 7] -> left: [5], root: 6, right: [7]

Many of the approaches here suggest slicing an array recursively and passing them. 
However, slicing the array is expensive. 
It is better to pass the left and right bounds into recursive calls instead.
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        def helper(left, right):
            if left > right:
                return None
            mid = (right + left)//2
            node = TreeNode(nums[mid])
            node.left = helper(left, mid-1)
            node.right = helper(mid+1, right)
            return node
        return helper(0, len(nums)-1)



