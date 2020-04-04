class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        
        def sumSurounding(i, j, board):
            s = 0
            # knowledge point
            # control the boarder line with min() and max()
            for m in range(max(0, i-1), min(i+2, len(board))):
                for n in range(max(0, j-1), min(j+2, len(board[0]))):
                    s += board[m][n]
            s -= board[i][j]
            return s
        
        row = len(board)
        col = len(board[0])
        
        #allocation of status memory  m * n
        status = [[0 for i in range(col)] for j in range(row)]
        
        #update status 
        for i in range(row):
            for j in range(col):
                status[i][j] = sumSurounding(i, j, board)
        
        #update board
        for i in range(row):
            for j in range(col):
                if board[i][j] == 1:
                    if status[i][j] < 2 or status[i][j] > 3:
                        board[i][j] = 0
                else:
                    if status[i][j] == 3:
                        board[i][j] = 1

s = Solution()
board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
s.gameOfLife(board)
print(board)
s.gameOfLife(board)
print(board)