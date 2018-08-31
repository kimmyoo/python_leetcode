"""
Given a sorted array nums, remove the duplicates in-place such that 
duplicates appeared at most twice and return the new length.
Do not allocate extra space for another array, you must do this by 
modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,1,1,2,3]
i=1           j i            j+=1, i+=1, A[0] = A[1]  counter = 1
      nums = [1,1,1,1,2,3]
i=2             j i          i+=1, counter = 1
      nums = [1,1,1,1,2,3]
i=3             j   i        i+=1, 
      nums = [1,1,1,1,2,3]
i=4             j     i      counter = 1, j+=1
      nums = [1,1,1,1,2,3]
i=4               j   i      A[2] =A[4]
      nums = [1,1,2,1,2,3]   
i=4               j   i      counter = 0
      nums = [1,1,2,1,2,3]   
i=5               j     i    j+=1
      nums = [1,1,2,1,2,3]
i=5                 j   i    A[3] = A[5]
      nums = [1,1,2,3,2,3]
                    j   i    counter = 0
return j = 3+1 =4.

Your function should return length = 3, with the first 4 elements of 
nums being 1, 1, 2, and 3 respectively.
It doesn't matter what you leave beyond the returned length.
"""

class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0
        j = 0
        counter = 0  # How many times repeated (1 for twice)
        n = len(A)
        for i in range(1, n):
            # if a repetitive element is encountered but counter is more than 0
            # only increment i (this is not explicit by looking at the if condition)
            if A[i] == A[j] and counter <= 0:
                j += 1
                A[j] = A[i]
                counter += 1 # if a repetitive element is encountered, increment counter
            #counter is greater than 0, repeated at least twice
            elif A[i] != A[j]:
                j += 1
                A[j] = A[i]
                counter = 0 # when a new element encountered, reset count
        return j + 1

"""
the counter <=0 and A[i]==A[j] condition will help increment i until elif is 
executed(locating a new element)
"""

s = Solution()
testList = [1, 1, 1, 1, 2, 3]
n = s.removeDuplicates(testList)
print("new length:", n)
