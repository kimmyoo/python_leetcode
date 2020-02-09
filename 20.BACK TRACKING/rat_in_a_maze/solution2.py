from __future__ import print_function
from __builtin__ import True
import time

class Solution(object):
    def solDisplay(self, sol):
        for r in sol:
            for ele in r:
                print(str(ele) + " ", end = "")
            print("")

    def isMoveValid(self, x, y, maze):
        """
        utility function to check if the current move is a valid move
        """
        height = len(maze)
        width = len(maze[0])
        if x >= 0 and x < width and y >= 0 and y < height and maze[y][x] == 0:
            return True
        return False
        
    def backTrackUtil(self, x, y, maze, sol):
        """
        rType: Bool
        """
        height = len(maze)
        width = len(maze[0])
        
        if x == width-1 and y == height-1:
            sol[y][x] = 1
            return True
        
        if self.isMoveValid(x, y, maze):
            sol[y][x] = 1
            #self.solDisplay(sol)
            #time.sleep(1)
            if self.backTrackUtil(x+1, y, maze, sol):
                return True
            if self.backTrackUtil(x, y+1, maze, sol):
                return True
            if self.backTrackUtil(x, y-1, maze, sol):
                return True
            sol[y][x] = 0
            return False

    def solveRatInMaze(self, maze):
        """
        type maze: list[list[int]]
        rtype: bool
        """
        
        if not maze:
            return False
        height = len(maze)
        width = len(maze[0])
        sol = [[0 for i in range(width)] for j in range(height)]
        self.solDisplay(sol)
        
        if self.backTrackUtil(0, 0, maze, sol):
            self.solDisplay(sol)
            return True
        return False


s = Solution()
newMaze = [[0, 1, 0, 1, 1, 0], 
           [0, 1, 1, 0, 0, 0],
           [0, 0, 0, 0, 1, 0], 
           [0, 1, 1, 1, 1, 0], 
           [0, 1, 1, 1, 1, 0], 
           [0, 0, 1, 1, 1, 0], 
           [1, 0, 0, 0, 0, 0]
          ]
s.solveRatInMaze(newMaze)