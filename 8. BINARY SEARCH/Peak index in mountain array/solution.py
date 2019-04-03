"""
Let's call an array A a mountain if the following properties hold:

A.length >= 3
There exists some 0 < i < A.length - 1 such that 
A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
Given an array that is definitely a mountain, return any i such that 
A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].
Example 1:

Input: [0,1,0]
Output: 1
Example 2:

Input: [0,2,1,0]
Output: 1
"""
class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        arr_size = len(A)
        left = 0
        right = arr_size -1
        
        while left < right:
            mid = left + (right - left)//2
            #print (left, mid, right)
            if A[mid] > A[mid-1]and A[mid] > A[mid+1]:
                return mid
            elif A[mid-1] < A[mid] and A[mid]< A[mid+1]:
                left = mid
            else:
                right = mid

#test
s = Solution()
A = [1, 2, 3, 7, 5, 4]
res = s.peakIndexInMountainArray(A)
print(res)
        
        
