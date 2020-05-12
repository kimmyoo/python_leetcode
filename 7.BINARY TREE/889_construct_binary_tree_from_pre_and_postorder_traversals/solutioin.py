# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # need to find out which nodes constitute left substree and right subtree
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        if not pre or not post:
            return None
        #first element is always the root
        root = TreeNode(pre[0])
        l = len(pre)
        # l == 1 edge case for single node or the deepest recursive calls for leaves
        if l == 1: return root
        # count of nodes in left substree 
        count = post.index(pre[1]) + 1
        root.left = self.constructFromPrePost(pre[1:count+1], post[:count])
        root.right = self.constructFromPrePost(pre[count+1:], post[count:-1])
        return root