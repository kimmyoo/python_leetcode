"""Implement an iterator over a binary search tree (BST). 
Your iterator will be initialized with the root node of a BST.
Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average 
O(1) time and uses O(h) memory, where h is the height of the tree."""


# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x, left, right):
        self.val = x
        self.left = left
        self.right = right

class BSTIterator(object):
    def __init__(self, root):
        self._arr = []
        self._inorder(root)
        self._cur = -1

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        # it makes sense to use list slicing here...
        if self._arr[self._cur+1:]:
            return True
        return False

    # @return an integer, the next smallest number
    def next(self):
        if self.hasNext():
            # since self_cur is incremented here, 
            # hasNext should not check single element self._arr[self._cur+1]
            # instead, use list slicing. list slicing will avoid out of boundary error
            self._cur += 1
            return self._arr[self._cur]

    def _inorder(self, root):
        if root is not None:
            if root.left is not None:
                self._inorder(root.left)
            self._arr.append(root.val)
            if root.right is not None:
                self._inorder(root.right)

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())

node5 = TreeNode(4, None, None)
node6 = TreeNode(7, None, None)
node4 = TreeNode(6, node5, node6)
node3 = TreeNode(1, None, None)
node2 = TreeNode(10, None, None)
node1 = TreeNode(3, node3, node4)
root = TreeNode(8, node1, node2)

i, v = BSTIterator(root), []
while i.hasNext():
    v.append(i.next())
print(v)

