# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def dfs(root):
            if not root:
                return (0, None)
            left, right = dfs(root.left), dfs(root.right)
            if left[0] > right[0]:
                return (left[0] + 1, left[1])
            elif right[0] > left[0]:
                return (right[0] + 1, right[1])
            else:
                return (left[0]+1, root)      
        return dfs(root)[1]


"""
if root == null, return pair(0, null)
left = deep(root.left)
right = deep(root.left)

if left depth == right depth,
deepest nodes both in the left and right subtree,
return pair (left.depth + 1, root)

if left depth > right depth,
deepest nodes only in the left subtree,
return pair (left.depth + 1, left subtree)

if left depth < right depth,
deepest nodes only in the right subtree,
return pair (right.depth + 1, right subtree)

"""