"""
Given an array A of integers, return true if and only if it is a valid mountain array.
Recall that A is a mountain array if and only if:
A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]
"""

class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) < 3:
            return False
        
        m = max(A)
        maxIndex = A.index(m)
        #edge cases
        if maxIndex == 0 or maxIndex == len(A)-1:
            return False
        
        for i in range(0, maxIndex):
            if A[i] >= A[i+1]:
                return False
        #right end stops 1 index to upper limit to check repeating elements at upper end
        for i in range(maxIndex, len(A)-1):
            if A[i] <= A[i+1]:
                return False
        return True