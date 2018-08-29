"""
Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9
to
     4
   /   \
  7     2
 / \   / \
9   6 3   1

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left, right):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        else:
            left = self.invertTree(root.left)
            right = self.invertTree(root.right)
            root.left = right
            root.right = left
            return root
    
    def inOrderTraversal(self, root):
        if root is None:
            return None
        else:
            if root.left is not None:
                print(root.left.val)
                self.inOrderTraversal(root.left)
            else:
                return
            print(root.val)
            if root.right is not None:
                print(root.right.val)
                self.inOrderTraversal(root.right)
            else:
                return


# test code
node_b = TreeNode(2, None, None)
node_a = TreeNode(1, None, None)
root = TreeNode(0, node_a, node_b)
s = Solution()
print("before inversion:")
s.inOrderTraversal(root)
s.invertTree(root)
print("-----I'm a segment line-------\nafter inversion:")

s.inOrderTraversal(root)


