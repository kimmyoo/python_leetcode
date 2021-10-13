# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    #my own solution. Learn recursive method!
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #subroutine to test palindrome pattern of temp list
        def isPalindrome(q):
            for i in range(len(q)//2):
                if q[i] != q[len(q)-1-i]:
                    return False
            return True
        
        if not root:
            return True
        q = []
        q.append(root)
        while q:
            temp = []
            for i in range(len(q)):
                curNode = q.pop(0)
                if curNode:
                    temp.append(str(curNode.val))
                    q.append(curNode.left) if curNode.left else q.append(None)
                    q.append(curNode.right) if curNode.right else q.append(None)   
                else:
                    temp.append("None")
#             print(temp)
#             for node in q:
#                 if node:
#                     print(node.val)
#                 else:
#                     print(node)
            if not isPalindrome(temp):
                return False
        return True
