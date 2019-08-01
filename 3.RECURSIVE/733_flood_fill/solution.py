class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        #get # of rows and # of cols
        rowCount = len(image)
        colCount = len(image[0])
        origColor = image[sr][sc]
        if origColor == newColor:
            return image
        
        def dfsFill(row, col):
            if image[row][col] == origColor:
                image[row][col] = newColor
                #don't forget to check list boundaries
                if row >=1:
                    dfsFill(row-1, col)
                if row <= rowCount-2:
                    dfsFill(row+1, col)
                if col >=1:
                    dfsFill(row, col-1)
                if col <= colCount-2:
                    dfsFill(row, col+1)
        dfsFill(sr, sc)
        return image

#test
s = Solution()
image = [[1,1,1],[1,1,0],[1,0,1]]
sr, sc = 1, 1
newColor = 9
res = s.floodFill(image, sr, sc, newColor)
print(res)

