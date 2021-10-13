# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class FindElements(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.s = set()
        def dfsRecover(root, val):
            if root:
                root.val = val
                if root.left:
                    root.left.val = root.val * 2 + 1
                    self.s.add(root.left.val)
                    dfsRecover(root.left, root.left.val)
                if root.right:
                    root.right.val = root.val * 2 + 2
                    self.s.add(root.right.val)
                    dfsRecover(root.right, root.right.val)
        if not root:
            return
        dfsRecover(root, 0)
        

    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        return target in self.s
        

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)