"""
Given two binary trees and imagine that when you put one of them to 
cover the other, some nodes of the two trees are overlapped while the 
others are not.

You need to merge them into a new binary tree. 
The merge rule is that if two nodes overlap,
then sum node values up as the new value of the merged node. 
Otherwise, the NOT null node will be used as the node of new tree.

Example 1:

Input: 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
Output: 
Merged tree:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7


Level order traversal 借助 Queue
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#~ if parent node is at index i in the array then the left child of that 
#~ node is at index (2*i + 1) 
#~ and right child is at index (2*i + 2) in the array.
def insertLevelOrder(A, root, i, n):
    """
    type i: int, i is the index of the parent node, 
            starting from 0 if insertion happens at root
    type n: int, n is the length of the array
    rtype: TreeNode
    """
    if i < n:
        #base case:
        tempNode = TreeNode(A[i])
        root = tempNode
        #~ print(root.val)
        #recursively insert to left and right
        root.left = insertLevelOrder(A, root.left, 2*i+1, n)
        root.right = insertLevelOrder(A, root.right, 2*i+2, n)
        return root

def levelOrderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List
    """
    if root is None:
        return []
    queue = []
    queue.append(root)
    output = []
    output.append(root.val)
    
    while len(queue) > 0:
        #pop() if no index is provide, will pop(-1) which is the last item in list
        currentNode = queue.pop(0)
        if currentNode is not None:
            # 按照层进行放置到queue里
            if currentNode.left is not None:
                queue.append(currentNode.left)
                output.append(currentNode.left.val)
            if currentNode.right is not None:
                queue.append(currentNode.right)
                output.append(currentNode.right.val)
    return output

# leetcode solution
def levelOrderList(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    result = []
    queue = []
    
    queue.append(root)
    while queue:
        queue_size = len(queue)
        i = 0
        level_result = []
        #use q_size to control level count
        while i < queue_size:
            node = queue.pop(0)
            if node:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                level_result.append(node.val)
            i += 1
        if level_result:
            result.append(level_result)
    return result

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None:
            return t2
        elif t2 is None:
            return t1
        else:
            root = TreeNode(t1.val + t2.val)
            root.left = self.mergeTrees(t1.left, t2.left)
            root.right = self.mergeTrees(t1.right, t2.right)
            return root
            # less space memory
            #~ t1.val += t2.val
            #~ t1.left = self.mergeTrees(t1.left, t2.left)
            #~ t1.right = self.mergeTrees(t1.right, t2.right)
            #~ return t1
        

#test code
s = Solution()
A = [43, 5, 6, 9, 9, 9, 100]
B = [6, 5, 2, 9, 10, 4, 7, 123, 45, 34, 21]

rootA = None
rootB = None
t1 = insertLevelOrder(A, rootA, 0, len(A))
t2 = insertLevelOrder(B, rootB, 0, len(B))
tMerged = s.mergeTrees(t1, t2)
print(tMerged.val, tMerged.left.val, tMerged.right.val, tMerged.left.left.val)
traversal = levelOrderTraversal(t2)
print (traversal)
traList = levelOrderList(t2)
print (traList)

