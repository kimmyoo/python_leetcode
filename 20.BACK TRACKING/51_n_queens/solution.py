class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def initBoard(n):
            b = [['.' for i in range(n)] for j in range(n)]
            return b

        def formatted(board):
            ans = []
            for row in board:
                ans.append("".join(row))
            return ans
        
        def display(board):
            for row in board:
                print(row)
            print("--")
        
        def isValid(board, r, c):
            #check each row 0 to r-1 at column c to see if there is any "Q"
            for i in range(r):
                if board[i][c] == 'Q': return False
            
            #diagonal
            i, j = r-1, c-1
            while i >= 0 and j >=0:
                if board[i][j] == 'Q': return False
                i-=1
                j-=1
            
            #diagonal
            i, j = r-1, c+1
            while i <= n-1 and j<=n-1:
                if board[i][j] == 'Q': return False
                i-=1
                j+=1
            return True
                    
        
        def backtrack(board, row):
            #if row == n that means the row has reached index n-1 
            if row == n:
                display(board)
                res.append(formatted(board))
                return 
            for col in range(n):
                if isValid(board, row, col):
                    board[row][col] = 'Q'
                    backtrack(board, row+1)
                    board[row][col] = '.'
        
        res = []
        board = initBoard(n)
        backtrack(board, 0)
        return res

s = Solution()
res = s.solveNQueens(4)
print(res)
