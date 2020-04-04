"""
Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell, 
where "adjacent" cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

Example:
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False
        
        height, width = len(board), len(board[0])
        for i in range(height):
            for j in range(width):
                if self.dfs(board, i, j, word, 0): return True
        return False
        
    def dfs(self, board, i, j, word, depth):
        height, width = len(board), len(board[0])
        if i < 0 or j < 0 or i == height or j == width or board[i][j] != word[depth]:
            return False
        #found a match
        if depth == len(word)-1:
            return True
        cur = board[i][j]
        #temporarily set current spot to 0 but later need to set it back to its original value
        board[i][j] = 0
        found = self.dfs(board, i+1, j, word, depth+1) or\
                self.dfs(board, i-1, j, word, depth+1) or\
                self.dfs(board, i, j+1, word, depth+1) or\
                self.dfs(board, i, j-1, word, depth+1)
        board[i][j] = cur
        return found