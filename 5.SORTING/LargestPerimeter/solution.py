"""
Given an array A of positive lengths, return the largest perimeter of a triangle with non-zero area, 
formed from 3 of these lengths.
If it is impossible to form any triangle of non-zero area, return 0
"""

class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # don't forget the reverse = True
        A.sort(reverse = True)
        perimeter = 0
        for i in range (0, len(A)-2):
            # since the list is sorted, we only check if the sum of the smaller numbers 
            # is greater than the large number
            if A[i] < A[i+1] + A[i+2]:
                    return A[i] + A[i+1] + A[i+2]
        return 0

#test code
s = Solution()
testA = [3, 4, 9, 1, 7]
res = s.largestPerimeter(testA)
print (res)
