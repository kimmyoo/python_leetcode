"""
Given an array nums, return true if the array was originally sorted in non-decreasing order, 
then rotated some number of positions (including zero). Otherwise, return false.
There may be duplicates in the original array.
Note: An array A rotated by x positions results in an array B of the same length such that A[i] == B[(i+x) % A.length], 
where % is the modulo operation.
"""
class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #repeat the array twice to find number of decreasing
        #if it's less than 3, return true
        numOfDec = 0
        for i in range(-len(nums)+1, len(nums)):
            if nums[i] < nums[i-1]:
                numOfDec += 1
        return numOfDec <= 2
    
    def check2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # improved version: instead of checking the array twice
        # simply do it from index -1, to index len(nums) - 1, 
        # so the number of decrease should be less than 2 if the array is non-decreasing
        numOfDec = 0
        for i in range(len(nums)):
            if nums[i-1] > nums[i]:
                numOfDec += 1
        return numOfDec < 2