class Solution(object):
    def removeLeafNodes(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode
        """
        #well.. return will recursively return its left or right child as None back to
        #its parent. if a parent becomes a leafy node because of return and also has target val
        #so this is why we check the left and right node first then the node itself.
        
        # isLeaf() is not actually necessary 
        def isLeaf(node):
            return not node.left and not node.right
        
        if root.left:
            root.left = self.removeLeafNodes(root.left, target)
        if root.right:
            root.right = self.removeLeafNodes(root.right, target)
        if isLeaf(root) and root.val == target: 
        # root.left == root.right means root.left == None and root.right ==None
            return None
        else:
            return root