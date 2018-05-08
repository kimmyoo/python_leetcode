"""
You are a product manager and currently leading a team to develop a new
product. Unfortunately, the latest version of your product fails the quality
check. Since each version is developed based on the previous version, all the
versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first
bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether
version is bad. Implement a function to find the first bad version. You should
minimize the number of calls to the API.
"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

def isBadVersion(test, n):
    return test[n-1]!=0

class Solution(object):
    def firstBadVersion(self, test, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        # here left +1 < right is import to make sure 
        # left and right doesn't overlap
        while left +1 < right:
            mid = left + (right - left)//2
            print (mid)
            if isBadVersion(test, mid):
                right = mid
            else:
                left = mid
        # after the loop stops, left and right are distinct 
        # test to see wheter let or right is the bad version.
        if isBadVersion(test, left):
            return left
        elif isBadVersion(test, right):
            return right




sample = [0, 0, 0, 0, 0, 0, 3, 4, 5, 6]

s = Solution()
print(s.firstBadVersion(sample, 10))


