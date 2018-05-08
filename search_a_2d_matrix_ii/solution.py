"""
Write an efficient algorithm that searches for 
a value in an m x n matrix.
This matrix has the following properties:
Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
For example,
Consider the following matrix:
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.
Given target = 20, return false.
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n = len(matrix) # number of rows
        m = len(matrix[0]) # number of columns 
        
        if target < matrix[0][0] or target > matrix[n - 1][m - 1]:
            return False
        # stepwise linear search from upper right or lower left
        # like mahattan block search....
        y = 0
        x = m - 1
        while x >= 0 and y <= n - 1:
            if target == matrix[y][x]:
                return True
            elif target < matrix[y][x]:
                x -= 1
            else:
                y += 1
        # if the program can run up to here, 
        # the while loop condition is checked at least 
        # either n or m times 
        # and no match is found, thus return false. 
        return False

        # 总结：
        # the trick here is the starting point.  
        # matrix [0][m-1] or matrix [n-1][0] are both fine.
        # the question asks to design an EFFICIENT algorithm
        # upper right corner or lower left will ensure the number of 
        # while condition checking is relatively low on a random basis

# tests tests tests go here!
a1 = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]

s = Solution()
print(s.searchMatrix(a1, 5))
print(s.searchMatrix(a1, 4))
print(s.searchMatrix(a1, 2018))
