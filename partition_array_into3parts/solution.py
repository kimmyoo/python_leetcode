class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        total = sum(A)
        if total % 3 == 0:
            s = total//3
            lower, upper = 0, len(A)-1
            lowerSum, upperSum = 0, 0
            middleSum = 0
            while lowerSum != s and lower <= upper-2:
                lowerSum += A[lower]
                lower+=1
            print (lower)
            #be careful about the condition, upper > lower
            while upperSum != s and upper > lower:
                upperSum += A[upper]
                upper-=1
            print(upper)
            while lower<=upper:
                middleSum += A[lower]
                lower+=1
            if middleSum == s:
                return True
            return False
        else:
            return False

s = Solution()
A = [3,1,3,1,3,1]
res = s.canThreePartsEqualSum(A)
print (res)