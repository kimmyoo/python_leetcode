# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        res = []
        to_delete = set(to_delete)
        res.append(root)

        def prune(root, t):
            if not root:
                return None
            if root.val == t.val:
                root = None
                return root
            root.left = prune(root.left, t)
            root.right = prune(root.right, t)
            return root
                
        def preOrder(root):
            if root:
                if root.val in to_delete:
                    cur = res.pop()
                    cur = prune(cur, root)
                    if root.left: res.append(root.left)
                    preOrder(root.left)
                    if root.right: res.append(root.right)
                    preOrder(root.right)
                    if cur: res.append(cur)
                    root = None
                else:
                    preOrder(root.left)
                    preOrder(root.right)
        preOrder(root)
        return res


    def delNodesB(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        credits: to Huahua
        """
        res = []
        ds = set(to_delete)
        
        def postOrderProcess(root):
            if not root:
                return None
            root.left = postOrderProcess(root.left)
            root.right = postOrderProcess(root.right)
            if root.val not in ds:
                return root
            #if root.val in ds, append newly created roots () to res;
            #if condition ensure None node is not added to res
            if root.left:
                res.append(root.left)
            if root.right:
                res.append(root.right)
            # if root.val in ds, return None to tell parent, this node now becomes None
            return None
        root = postOrderProcess(root)
        if root: res.append(root)
        return res