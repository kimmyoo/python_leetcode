class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        n = len(A)
        res = [0] * n
        i = 0
        j = n -1
        for p in range (n-1, -1, -1):
            if abs (A[i]) >= abs (A[j]):
                res[p] = A[i] * A[i]
                i+=1
            else:
                res[p] = A[j] * A[j]
                j-=1
        return res

#test
s = Solution()
A = [-4,-1,1,3,10]
res = s.sortedSquares(A)
print(res)
