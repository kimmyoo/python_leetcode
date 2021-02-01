class Solution:
    def __init__(self):
        #self.star = 0
        self.res = 0

    def numEnclaves(self, A):
        w = len(A)
        h = len(A[0])
    
        def dfsPutAsterisk(x, y):
            A[x][y] = "*"
            #self.star += 1
            # we put an "*", we need to update self.res
            self.res -= 1
            if x+1 < w and A[x+1][y]==1:
                dfsPutAsterisk(x+1, y)
            if y+1 < h and A[x][y+1]==1:
                dfsPutAsterisk(x, y+1)
            if x > 0 and A[x-1][y]==1:
                dfsPutAsterisk(x-1, y)
            if y > 0 and A[x][y-1]==1:
                dfsPutAsterisk(x, y-1)
        
        for i in range (w):
            for j in range(h):
                if A[i][j]:
                    self.res +=1
                #we are on the edges, 
                if i == 0 or j == 0 or i == w-1 or j == h-1:
                    #dfs starts on edges when we see a "1"
                    if A[i][j]==1: 
                        dfsPutAsterisk(i, j)
        #return self.res -self.star
        return self.res

obj = Solution()
A = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
res = obj.numEnclaves(A)
print(res)