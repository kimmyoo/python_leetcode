# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.st = []
        while root:
            self.st.append(root)
            # the pointer is initiated to the leftmost node's left child which is None
            root = root.left

    def next(self):
        """
        :rtype: int
        """
        cur = self.st.pop()
        x = cur.right
        while x:
            # save the next smallest node to stack
            self.st.append(x)
            # need to walk to leftmost node of the subtree which is the next smallest node
            x = x.left
        return cur.val
 

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.st) > 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()