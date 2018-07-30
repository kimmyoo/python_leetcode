"""
Given a binary tree, return the preorder, postorder, inorder traversal 
of its nodes' values.

    1
   / \
  3   2
     /
    3
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left, right):
        self.val = x
        self.left = left
        self.right = right


class Solution(object):

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        path = []
        if root is None:
            return path
        stack = []
        stack.append(root)
        while stack:
            root = stack.pop()
            path.append(root.val)
            #~ Push the root onto the stack.
            #~ While the stack is not empty
            #~ pop the stack and visit it
            #~ push its two children (right then left, so when visiting the node by popping 
            #~ the order is left to right ensure the correct order)
            if root.right is not None:
                stack.append(root.right)
            if root.left is not None:
                stack.append(root.left)
        return path

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        path = []
        if root is None:
            return path
        stack1 = []
        stack2 = []
        stack1.append(root)
        while stack1:
            root = stack1.pop()
            stack2.append(root.val)
            #如果忘了顺序可以用三个 node 来举个例子
            #    1       | |  | |
            #   3 2      | |  | |
            
            #            | |  | |
            #            |1|  | |
            #
            #            |2|  | |
            #            |3|  |1|
            #
            #            | |  |2|
            #            |3|  |1|
            #
            #                 |3|
            #            | |  |2| 
            #            | |  |1|   don't forget to pop nodes 
            if root.left is not None:
                stack1.append(root.left)
            if root.right is not None:
                stack1.append(root.right)
        while stack2:
            path.append(stack2.pop())
        return path

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
node3 = TreeNode(3, None, None)
node2 = TreeNode(2, node3, None)
node1 = TreeNode(3, None, None)
root = TreeNode (1, node1, node2)

s = Solution ()
path = s.preorderTraversal(root)
print(path)
path = s.postorderTraversal(root)
print(path)
path = s.inorderTraversal(root)
print(path)
