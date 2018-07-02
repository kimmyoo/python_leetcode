"""
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        path = []
        if root is None:
            return path
        stack = []
        while stack or root is not None:
            if root is not None:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                path.append(root.val)
                root = root.right
        return path

#test 
root = TreeNode(1)
node0 = TreeNode(0)
node1 = TreeNode(2)
node2 = TreeNode(3)
root.right = node1
root.left = node0
node1.left = node2

#stack: root          root.left: node0           path:
#stack: root, node0   root.left: None            path:
#stack: root                                     path: 0,         root = None
#stack:                                          path: 0, 1       root = node1
#stack: node1         root.left: node2           path: 0, 1
#stack: node1, node2  root.left: None            path: 0, 1
#stack: node1,                                   path: 0, 1, 3    root = None
#stack:                                          path: 0, 1, 3, 2 root = None
#condition check breaks the while loop         

s = Solution()
path = s.inorderTraversal(root)
print (path)


