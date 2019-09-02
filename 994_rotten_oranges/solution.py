class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #my stupid solution
        r, c = len(grid), len(grid[0])
        def infect(i, j):
            #top
            if i-1 >= 0:
                if grid[i-1][j] == 1:
                    grid[i-1][j] = 2
                    self.goodCount -=1
                    self.badCount +=1
                    self.newlyInfected.add((i-1, j))
            #bottom
            if i+1 <= r-1:
                if grid[i+1][j] == 1:
                    grid[i+1][j] = 2
                    self.goodCount -=1
                    self.badCount +=1
                    self.newlyInfected.add((i+1, j))
            #left
            if j-1 >= 0:
                if grid[i][j-1] == 1:
                    grid[i][j-1] = 2
                    self.goodCount -=1
                    self.badCount +=1
                    self.newlyInfected.add((i, j-1))
            #right
            if j+1 <= c -1:
                if grid[i][j+1] == 1:
                    grid[i][j+1] = 2
                    self.goodCount-=1
                    self.badCount+=1
                    self.newlyInfected.add((i, j+1))
        
        self.goodCount = 0
        self.stepCount = 0
        self.badCount = 0
        self.newlyInfected = set()
        
        for l in grid:
            for e in l:
                if e == 1:
                    self.goodCount+=1
                if e == 2:
                    self.badCount+=1
        #edge case 
        if self.goodCount == 0:
            return 0
        
        while True:
            bad = self.badCount
            for i in range(r):
                for j in range(c):
                    if grid[i][j] == 2 and (i, j) not in self.newlyInfected:
                        infect(i, j)
            self.stepCount +=1
            self.newlyInfected.clear()
            if self.goodCount == 0:
                return self.stepCount
            #this is to see if the rot process is still going on
            if bad == self.badCount:
                break
        #if still some good oranges left uninfected
        if self.goodCount > 0:
            return -1

        return self.stepCount-1

s = Solution()
grid1 = [[2,1,1],[1,1,0],[0,1,1],[2,1,1],[1,1,0],[0,1,1]]
grid2 = [[2,1,1],[1,1,0],[0,1,1]]
res1 = s.orangesRotting(grid1)
res2 = s.orangesRotting(grid2)
print(res1, res2)



