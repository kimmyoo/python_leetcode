"""
Given a binary tree, return all root-to-leaf paths.
For example, given the following binary tree:
   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:
["1->2->5", "1->3"]
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, lChild, rChild):
        self.val = x
        self.left = lChild
        self.right = rChild

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        cand = []
        self.binary_tree_paths(root, cand, res)
        return res

    def binary_tree_paths(self, root, cand, res):
        if root is None:
            return
        else:
            cand.append(root.val)
            print(cand)
            # this line check if the current node is a leaf node
            if root.left is None and root.right is None:
                #use map() to convert each item in the list to
                # a string, and then join them:
                p = '->'.join(map(str, cand))
                res.append(p)
                #print (res)
            self.binary_tree_paths(root.right, cand, res)
            self.binary_tree_paths(root.left, cand, res)
            # pop() will pop the current node out of cand 
            #(forget the node in the curren path until the new leaf node is encountered)
            cand.pop()
            print (cand)

#test of the algorithm
"""
    N
  /   \
  a    o
   \
    h
cand ['N',]           res []
cand ['N', 'o']       res ['N->o', ]
cand ['N']            res ['N->o', ]
cand ['N', 'a', ]     res ['N->o', ]
cand ['N', 'a', 'h']  res ['N->o', 'N->a->h', ]
cand ['N', 'a']       res ['N->o', 'N->a->h', ]
cand ['N']            res ['N->o', 'N->a->h', ]
cand ['N']
"""
node3 = TreeNode('h', None, None)
node2 = TreeNode('a', None, node3)
node1 = TreeNode('o', None, None)
root = TreeNode('N', node2, node1)

s = Solution()
res = s.binaryTreePaths(root)
for ele in res:
    print (ele)
