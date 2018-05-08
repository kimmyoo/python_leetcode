# -*- coding: utf-8 -*-
"""
A peak element is an element that is greater than its neighbors.
Given an input array where num[i] ≠ num[i+1], find a peak element and return
its index.
The array may contain multiple peaks, in that case return the index to any one
of the peaks is fine.
You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function
should return the index number 2.

Note:
Your solution should be in logarithmic complexity.
"""

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        left = 0
        right = n - 1
        if n == 1:
            return 0
        while left <= right:
            mid = left + (right - left) // 2
            # mid == 0 is 0 + 0, so right - left is 1, so right is 1
            # left is 0, only two elements: nums[0] and nums[1]
            # and num[0] > num[1]
            if mid == 0 and nums[mid] > nums[mid + 1]:
                return mid
            # the last element, and the last element > previous one
            # return the last element's index
            elif mid == n - 1 and nums[mid] > nums[mid - 1]:
                return mid
            
            elif nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid
            elif mid > 0 and nums[mid + 1] > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return mid


#num[i] ≠ num[i+1]
a1 = [1, 2]
a2 = [2, 6, 2, 9, 2, 9,1]
s = Solution()
print(s.findPeakElement(a1))
print(s.findPeakElement(a2))
