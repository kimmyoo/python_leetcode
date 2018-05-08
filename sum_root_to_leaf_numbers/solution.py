"""
Given a binary tree, where every node value is a Digit from 1-9 .
Find the sum of all the numbers which are formed from root to 
leaf paths.
For example consider the following Binary Tree.
                                        6
                                      /   \
                                    3       5
                                  /   \       \
                                 2     5        4  
                                      /   \
                                     7     4
  There are 4 leaves, hence 4 root to leaf paths:
   Path                    Number
  6->3->2                   632
  6->3->5->7               6357
  6->3->5->4               6354
  6->5>4                    654   
Answer = 632 + 6357 + 6354 + 654 = 13997 
"""


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x, left, right):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        self.res = 0  # global variable for sum
        num = 0
        self.sn(root, num)
        return self.res

    # this recursive method is to update global variable 
    def sn(self, root, num):
        if root is None:
            return #this is where recursion stops
        elif root.left is None and root.right is None:
            num += root.val #get the number of the current node(leaf)
            self.res += num
        else: # if curren node has a left or right child
            num += root.val #get the number of current node
            self.sn(root.left, 10 * num)# multiply by 10 then recursion
            self.sn(root.right, 10 * num)

# tests
#           root(1)
#          /      \
#      node1(5)   node2(1)
#        /   \    
#  node3(6)  node4(3)
#                          156 + 153 + 11 = 320

node3 = TreeNode(6, None, None)
node4 = TreeNode(3, None, None)
node1 = TreeNode(5, node3, node4)
node2 = TreeNode(1, None, None)
root = TreeNode(1, node1, node2)
s = Solution()
res = s.sumNumbers(root)
print (res)

