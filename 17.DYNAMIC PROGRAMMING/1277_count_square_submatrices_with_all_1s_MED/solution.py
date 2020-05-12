"""
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.
Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
"""
class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        h, w = len(matrix), len(matrix[0])
        if h == 0:
            return 0
        
        res = 0
        for i in range(h):
            for j in range(w):
                if matrix[i][j] == 0:
                    continue
                # border elements
                if i == 0 or j == 0:
                    res += 1
                #inner elements
                else:
                    #transition relation
                    matrix[i][j] = min(matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1]) + 1
                    res += matrix[i][j]
        return res