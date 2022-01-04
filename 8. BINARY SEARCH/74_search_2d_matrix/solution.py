class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # this solution is not optimal time complexity is m+n
        padding = [matrix[0][0]] * len(matrix[0])
        matrix.insert(0, padding)
        x, y = len(matrix)-1, len(matrix[0])-1
        
        while (x >= 0 and y >= 0):
            if (target < matrix[1][0] or target > matrix[x][y]):
                return False
            if target == matrix[x][y]: 
                return True
            elif matrix[x-1][y] >= target:
                x-=1
            else:
                y-=1