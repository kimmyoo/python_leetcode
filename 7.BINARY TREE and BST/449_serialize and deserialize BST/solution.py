# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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
        
    def preOrderTraversalDisplay(self, root):
        if root:
            print(root.val)
            self.preOrderTraversalDisplay(root.left)
            self.preOrderTraversalDisplay(root.right)

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def preOrderTraversal(root, container):
            if root:
                container.append(root.val)
                preOrderTraversal(root.left, container)
                preOrderTraversal(root.right, container)
            else:
                container.append("None")
            return container

        container = []
        if root:
            lstRepr = preOrderTraversal(root, container)
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
            print(data)
            lstRepr = data.split(',')
            return self.preorderBuildFromArray(lstRepr)
        else:
            return None


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans

arr = ["10", "5", "3", "None", "None", "7", "None", "None", "15", "None", "None", "20", "None", "None"]

ser = Codec()
deser = Codec()
root = ser.preorderBuildFromArray(arr)

serializedTree = ser.serialize(root)
print("serialized:", serializedTree)
deserializedTree = deser.deserialize(serializedTree)

ser.preOrderTraversalDisplay(deserializedTree)
