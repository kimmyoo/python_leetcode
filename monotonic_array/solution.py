class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        monoIncrease = False
        monoDecrease = False
        
        i = 0
        while i <= len(A)-2:
            if A[i+1] == A[i]:
                i+=1
            elif A[i+1] > A[i]:
                monoIncrease = True
                i+=1
            else:
                monoDecrease = True
                i+=1
            if monoIncrease == True and monoDecrease == True:
                return False
        return True



s = Solution()
testArr1 = [1, 3, 5, 6, 7]
testArr2 = [3, 3, 2, 1, 0, -1]
testArr3 = [1, 3, -1]

res1 = s.isMonotonic(testArr1)
res2 = s.isMonotonic(testArr2)
res3 = s.isMonotonic(testArr3)

print (res1, res2, res3)
