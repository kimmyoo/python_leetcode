"""
Given an array of integers nums sorted in ascending order, 
find the starting and ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].
Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
"""
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = self.findLeft(nums, target), self.findRight(nums, target)
        return [l, r]
    
    def findRight(self, nums, t):
        start, end = 0, len(nums)-1
        index = -1
        while start <= end:
            mid = (start+end)//2
            # shift to right half until start == end
            # [5,7,7,8,8,10]   target is 8, mid is 2, nums[2] <= target
            if nums[mid] <= t:
                start = mid + 1
            else:
                end = mid -1
            if nums[mid] == t:
                index = mid
        return index
    
    def findLeft(self, nums, t):
        start, end = 0, len(nums)-1
        index = -1
        while start <= end:
            mid = (start+end)//2
            if nums[mid] >= t:
                end = mid - 1
            else:
                start = mid + 1
            if nums[mid] == t:
                index = mid
        return index
    