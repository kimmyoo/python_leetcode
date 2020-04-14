class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        the tricky part is for eles that falls on the the diagonal, the diff of i, j, ie. i-j
        is the same. so we use a list dict and put eles on the same diagonal to list, then sort
        then put them back to their correct positions.
        """
        d = collections.defaultdict(list)
        width, height = len(mat[0]), len(mat)
        
        for i in range(height):
            for j in range(width):
                d[i-j].append(mat[i][j])
        
        for k in d:
            d[k].sort(reverse=True)
        
        for i in range(height):
            for j in range(width):
                mat[i][j] = d[i-j].pop()
            
        return mat