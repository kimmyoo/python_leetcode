class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        height = len(grid)
        width = len(grid[0])

        def backtracking(i, j):
            #if we go over boarder or we meet a grid with value of 0
            if i < 0 or i == height or j == width or j < 0 or grid[i][j] == 0:
                return 0
            #remember the current because i will be replacing the grid[i][j] with 0
            current = grid[i][j]
            s = 0
            #mark visited as 0 to avoid going back: learn this trick
            grid[i][j] = 0
            for x, y in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                s = max(s, backtracking(x, y))
            grid[i][j] = current #backtracking
            #don't forget to add current
            return s + current
            
        res = 0
        # do backtracking starting from each ele in matrix
        for x in range(height):
            for y in range(width):
                #new learned trick: rolling update max or min
                res = max(res, backtracking(x,y))
        #print(res)
        return res

s = Solution()
inputList = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
ans = s.getMaximumGold(inputList)
print("answer is: {}".format(ans))