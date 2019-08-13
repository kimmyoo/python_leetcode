"""
Given an m * n matrix M initialized with all 0's and several update operations.
Operations are represented by a 2D array, 
and each operation is represented by an array with two positive integers a and b, 
which means M[i][j] should be added by one for all 0 <= i < a and 0 <= j < b.
You need to count and return the number of maximum integers in the matrix after performing all the operations.
"""
class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if not ops:
            return m*n
        x = [op[0] for op in ops]
        y = [op[1] for op in ops]
        return min(x)*min(y)

    def maxCount2(self, m, n, ops):
        if not ops:
            return m * n
        x, y = zip(*ops) # learn zip tricks
        print(x, y)
        return min(x) * min(y)
# test
s = Solution()
m = 30
n = 20
ops = [[15,5],[9,16]]
res = s.maxCount(m, n, ops)
print(res)

