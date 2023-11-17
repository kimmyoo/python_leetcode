# Definition for a binary tree node.
from treeSetup import Codec, preOrderTraversalDisplay, TreeNode


class Solution:
    def inorderTraversalToArray(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def inorder(root, container):
            if root:        
                inorder(root.left, container)
                container.append(root.val)
                inorder(root.right, container)
            return container
        
        res = []

        return inorder(root, res)

    # iterative
    def inorderTraversal2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        res = []
        if not root: 
            return res
        
        stack = []

        curNode = root
        while curNode or stack:
            # this while loop end when encouters None
            while curNode:
                stack.append(curNode)
                curNode = curNode.left
            curNode = stack.pop()
            res.append(curNode.val)
            curNode = curNode.right
        
        return res

    # iterative 
    def preorder_traversal(self, root):
        res = []
        if not root:
            return res
    
        stack = [root]
        while stack:
            curr_node = stack.pop()
            res.append(curr_node.val)
            # put root.right to bottom of stack
            # so our left subtree of current node is on top
            if curr_node.right:
                stack.append(curr_node.right)
            if curr_node.left:
                stack.append(curr_node.left)
        return res
    








arr = ["10", "5", "3", "None", "None", "7", "None", "None", "15", "None", "None", "20", "None", "None"]

ser = Codec()
deser = Codec()
root = ser.preorderBuildFromArray(arr)

serializedTree = ser.serialize(root)
print("serialized:", serializedTree)
deserializedTree = deser.deserialize(serializedTree)

preOrderTraversalDisplay(deserializedTree)
