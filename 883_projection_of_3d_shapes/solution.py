class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        
        l = len(grid)
        w = len(grid[0])
        
        zeroCount = 0
        xzMax = []
        yzMax = [0] * w
        for i in range(l):
            xzMax.append(max(grid[i]))
            for j in range(w):
                if grid[i][j] == 0:
                    zeroCount+=1
                yzMax[j] = max(grid[i][j], yzMax[j])

        top = l * w - zeroCount
        front = sum(xzMax)
        side = sum(yzMax)
        return top + front + side

s = Solution()
grid = [[1,2],[3,4]]
res = s.projectionArea(grid)
print(res)
