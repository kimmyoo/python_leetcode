"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, 
find the one that is missing from the array.
"""
class Solution(object):
    # leetcode solution using math trick
    def missingNumber1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total = n * (n+1) / 2
        t = 0
        for num in nums:
            t += num
        return total - t
    
    # my own solution. it's not a linear solution because of sorting is used
    def missingNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        nums.sort()
        #here l + 1
        for i in range(l+1):
            #here need to check if the missing num is the last integer (the greatest one)
            if i == l:
                return l
            if nums[i] != i:
                return i

    #prefer this one
    def missingNumber3(self, nums):
        num_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number





