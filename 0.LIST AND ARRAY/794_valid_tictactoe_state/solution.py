class Solution(object):
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
    
        def getWinner (b):
            winner = set()
            for i in range(3):
                # all X in a row
                if sum(b[i]) == -3:
                        winner.add("O")
                # all O in a row
                if sum(b[i]) == 3:
                    if "X" not in winner:
                        winner.add("X")
                
            for j in range(3):
                if(b[0][j]+b[1][j]+b[2][j]) == -3:
                    winner.add("O")
                if(b[0][j]+b[1][j]+b[2][j]) == 3:
                    winner.add("X")
        
            if b[0][0] + b[1][1] + b[2][2] == -3 or b[2][0] + b[1][1] + b[0][2] == -3:
                winner.add("O")
            if b[0][0] + b[1][1] + b[2][2] == 3 or b[2][0] + b[1][1] + b[0][2] == 3:
                winner.add("X")
            
            return winner



        listBoard = []
        for str in board:
            temp = [ c for c in str]
            for i in range(3): 
                if temp[i] == 'X':
                    temp[i] = 1
                elif temp[i] == 'O':
                    temp[i] = -1
                else:
                    temp[i] = 0
            listBoard.append(temp)

        stateVal = sum (sum(x) for x in listBoard)
        winner = getWinner(listBoard)

        print(winner)
        # x is at most one more than o
        # x is at most one less than x
        if stateVal <= -1 or stateVal >=2:
            return False
        
        # 2 winners not possible
        if len(winner) == 2:
            return False
        
        # one winner
        if len(winner) == 1:
            if winner.pop() == 'X':
                return stateVal == 1
            else:
                return stateVal == 0
        else:
            return True



s = Solution()
board = ["OOO","XXO","XXX"]
res = s.validTicTacToe(board)
print(res)