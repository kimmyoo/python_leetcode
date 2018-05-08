"""
Given a binary tree, check whether it is a mirror of itself
(ie, symmetric around its center).
For example, this binary tree is symmetric:
    1
   / \
  2   2
 / \ / \         
3  4 4  3
But the following is not:
    1
   / \
  2   2
   \   \
   3    3
"""
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

def height(node):
    if node is None:
        return 0
    else:
        lheight = height (node.left)
        rheight = height (node.right)
        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1

def printGivenLevel(root, level):
    if root is None:
        return
    if level == 1:
        print(root.val)
    elif level > 1:
        printGivenLevel(root.left, level-1)
        printGivenLevel(root.right, level-1)

def printLevelOrder(root):
    h = height(root)
    for i in range(1, h+1):
        printGivenLevel(root, i)
        
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # take care of exception, empty tree
        if root is None:
            return True
        # first level symmetry 
        if root.left is None and root.right is None:
            return True
        # next level, recursion starts here
        if root.left is not None and root.right is not None:
            return self._isSymmetric(root.left, root.right)
        return False

    # recursive function 
    def _isSymmetric(self, left, right):
        if left is None and right is None:
            return True
        if left is not None and right is not None:
            return (left.val == right.val and
                    self._isSymmetric(left.left, right.right) and
                    self._isSymmetric(left.right, right.left))
        # the last line deals with asymmetrical leaves
        return False
#test goes here
#create a bunch of nodes and construct a tree
root = TreeNode('大')
node1 = TreeNode('盘')
node2 = TreeNode('盘')
node3 = TreeNode('鸡')
node4 = TreeNode('鸡')
node5 = TreeNode('肉')
node6 = TreeNode('肉')

root.left = node1
root.right = node2
node1.left = node3
node1.right = node5
node2.left = node6
node2.right = node4

s = Solution()
res = s.isSymmetric(root)
printLevelOrder(root)
print(res)


