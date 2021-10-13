# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
Intuition:
Nodes are cousins if they have the same depth but different parents. 
A straightforward approach is to be able to know the parent and depth of each node.

Algorithm:
We can use a depth-first search to annotate each node. 
For each node with parent par and depth d, 
we will record results in hashmaps: parent[node.val] = par and depth[node.val] = d.
"""
class Solution(object):
    def __init__(self):
        self.parent = {}
        self.depth = {}
        
    def dfsToMap(self, node, par = None):
        if node:
            #if the node is root node, depth is initialized to 0 else increment 1
            self.depth[node.val] = self.depth[par.val] + 1 if par else 0
            self.parent[node.val] = par
            self.dfsToMap(node.left, node)
            self.dfsToMap(node.right, node)
            
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        self.dfsToMap(root)
        return self.depth[x] == self.depth[y] and self.parent[x]!=self.parent[y]

