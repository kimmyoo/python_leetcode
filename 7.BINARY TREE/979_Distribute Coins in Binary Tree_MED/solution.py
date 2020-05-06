# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        
        #recursive call reached to the leftmost leaf
        #finish the left subtree of the root then move to the right subtree
        #finally the getBalance return 0 because the val of the root will be 1 thus balance is 0
        def getBalance(node):
            if not node:
                return 0
            l = getBalance(node.left)
            r = getBalance(node.right)
            #we use abs() to calculate the flow through the edges
            self.res += abs(l) + abs(r)
            #current balance is current val of node minus 1 which is needed by itself
            #and plus the the coins coming from children (either minor or plus)
            return node.val - 1 + l + r
        
        getBalance(root)
        return self.res
