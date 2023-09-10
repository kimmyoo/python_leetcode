class Solution(object):
    # exceeds time limit 超时解法
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        height, width = len(mat), len(mat[0])
        
        res  = [[0]*width for i in range(height)]
        rowSum = [sum(mat[i]) for i in range(height)]
        totalSum = sum(rowSum)
        # print(totalSum)
        
        def isEdge(i, j):
            return (mat[max(0, i-1)][j] == 0 or mat[min(i+1, height-1)][j] == 0 or mat[i][max(0, j-1)] == 0 or mat[i][min(width-1, j+1)] == 0)
        
        def modEdge(i, j):
            if mat[i][j] == -1:
                mat[i][j] = 0
  
        while totalSum > 0:
            for i in range(height):
                if rowSum[i] > 0:
                    for j in range(width):
                        if mat[i][j] == 1:
                            res[i][j] += 1
                            if isEdge(i, j):
                                mat[i][j] = -1
                                rowSum[i] -= 1
                                totalSum -= 1
            # print(mat)
            for i in range(height):
                for j in range(width):
                    modEdge(i, j)
        return res

    # accepted solution 
    def updateMatrix2(self, mat):
        height, width = len(mat), len(mat[0])
        res  = [[float('inf')]* width for i in range(height)]
        
        for i in range(height):
            for j in range(width):
                # first pass needs to find 0s
                if mat[i][j] == 0:
                    res[i][j] = 0
                else:
                    if i > 0:
                        res[i][j] = min(res[i][j], res[i-1][j] + 1)
                    if j > 0:
                        res[i][j] = min(res[i][j], res[i][j-1] + 1)
        # print(res)
        
        for i in range(height-1, -1, -1):
            for j in range(width-1, -1, -1):
                # in second pass, the lower boundary is base case 0 and 1
                # if a value in res is 0 or 1, you cann't make it even less
                # 一种是当值为0时，还有一种是当值为1时，这两种情况下值都不可能再变小了，所以没有更新的必要
                if res[i][j] != 0 and res[i][j] != 1:
                    if i < height - 1:
                        res[i][j] = min(res[i][j], res[i+1][j] + 1) 
                    if j < width -1 :
                        res[i][j] = min(res[i][j], res[i][j+1] + 1)

        # print(res)

        return res





s = Solution()

testCase = [[0,1,1,1,1,1,1,1,1,1,1,0], [1,1,1,1,1,0,1,1,1,1,1,0], [1,1,1,1,0,1,1,1,1,1,1,0]]

res = s.updateMatrix2(testCase)
print(res)


        