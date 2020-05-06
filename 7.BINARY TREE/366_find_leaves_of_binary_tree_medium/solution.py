class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        while root:
            leaves = []
            root = self.dfsRemove(root, leaves)
            res.append(leaves)
        return res
            
        
    def dfsRemove(self, root, leaves):
        if not root:
            return None
        if not root.left and not root.right:
            leaves.append(root.val)
            return None
        root.left = self.dfsRemove(root.left, leaves)
        root.right = self.dfsRemove(root.right, leaves)
        #remember to return root!
        return root
    
    def preOrder(self, root):
        if root:
            print(root.val)
        if root.left:
            self.preOrder(root.left)
        if root.right:
            self.preOrder(root.right)



root = TreeNode(10)
node1 = TreeNode(8)
node2 = TreeNode(9)
node3, node4 = TreeNode(5), TreeNode(6)
node1.left, node1.right = node3, node4
root.left, root.right = node1, node2

s = Solution()
#s.preOrder(root)
ans = s.findLeaves(root)
print(ans)


                    
        