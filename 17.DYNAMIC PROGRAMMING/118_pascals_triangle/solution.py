"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
"""
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        tri = []
        for i in range(numRows):
            #throwaway variable '_': i don't care the value of this particular variable
            temp = [None for _ in range(i+1)]
            temp[0], temp[-1] = 1, 1
            #inner for loop to fill each level from index 1 to second to the last element
            #for loop will be skipped if i <= 1
            for j in range(1, i):
                temp[j] = tri[i-1][j-1] + tri[i-1][j]
            tri.append(temp)
        return tri


s = Solution()
res = s.generate(9)
for row in res:
    print(row)
