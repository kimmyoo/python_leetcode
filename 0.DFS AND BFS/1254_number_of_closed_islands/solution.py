class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        h = len(grid)
        w = len(grid[0])
        res = 0
        
        def dfs(x, y, target, char):
            grid[x][y] = char
            if x+1 < h and grid[x+1][y]==target:
                dfs(x+1, y,target, char)
            if x-1 > 0 and grid[x-1][y]==target:
                dfs(x-1, y,target, char)
            if y+1 < w and grid[x][y+1]==target:
                dfs(x, y+1,target, char)
            if y-1 > 0 and grid[x][y-1]==target:
                dfs(x, y-1,target, char)

        for i in range(h):
            for j in range(w):
                if i == 0 or j == 0 or i == h-1 or j == w-1:
                    if grid[i][j] == 0:
                        dfs(i, j, 0, 1)
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 0:
                    res += 1
                    dfs(i, j, 0, "*")
        return res