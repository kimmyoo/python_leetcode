"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as
a binary tree in which the depth of the two subtrees of
every node never differ by more than 1.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left, right):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        else:
            # the if condition is recursive, the return statment is also recursive.
            if self.isBalanced(root.left) and self.isBalanced(root.right):
                return abs(self.depth(root.left) - self.depth(root.right)) <= 1
            else:
                return False

    def depth(self, root):
        if root is None:
            return -1
        else:
            return max(self.depth(root.left), self.depth(root.right)) + 1


# test code
node_b = TreeNode(2, None, None)
node_a = TreeNode(1, None, None)
root = TreeNode(0, node_a, node_b)

s = Solution()
print(s.isBalanced(root))


