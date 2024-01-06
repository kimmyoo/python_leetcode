from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right




class Codec:
    def preorderBuildFromArray(self, arr):
        if arr:
            ch = arr.pop(0)
            if ch == "None":
                return None
            root = TreeNode(ch)
            root.left = self.preorderBuildFromArray(arr)
            root.right = self.preorderBuildFromArray(arr)
            return root
        

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        def _preOrderHelper(root, container):
            if root:
                container.append(root.val)
                _preOrderHelper(root.left, container)
                _preOrderHelper(root.right, container)
            else:
                container.append("None")
            return container
        
        
        container = []
        if root:
            lstRepr = _preOrderHelper(root, container)
            lstRepr = [ str(lstRepr[i]) for i in range(len(lstRepr))]
            strRepr = ','.join(lstRepr)
            return strRepr
        else:
            return ""


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) > 0:
            lstRepr = data.split(',')
            return self.preorderBuildFromArray(lstRepr)
        else:
            return None




def preOrderTraversalDisplay(root):
    if root:
        print(root.val)
        preOrderTraversalDisplay(root.left)
        preOrderTraversalDisplay(root.right)
