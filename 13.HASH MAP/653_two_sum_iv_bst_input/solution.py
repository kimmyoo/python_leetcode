# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""
set, queue, breath-first search
"""
import collections

class Solution(object):
    def findTarget(self, root, k):
        s = set()
        de = collections.deque()
        de.append(root)
        while de:
            #get the leftmost element
            cur = de.popleft()
            t = k - cur.val
            if t in s:
                return True
            else:
                s.add(cur.val)
            if cur.left:
                de.append(cur.left)
            if cur.right:
                de.append(cur.right)
        return False

n1 = TreeNode(6)
n2 = TreeNode(3)
n3 = TreeNode(8)
n4 = TreeNode(1)
n5 = TreeNode(4)
n6 = TreeNode(7)
n7 = TreeNode(9)

n2.left = n4
n2.right = n5

n3.left = n6
n3.right = n7

n1.left = n2
n1.right = n3

s = Solution()
res = s.findTarget(n1, 16)
res2 = s.findTarget(n1, 18)
print(res, res2)