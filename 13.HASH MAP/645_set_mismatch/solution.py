"""
The set S originally contains numbers from 1 to n. 
But unfortunately, due to the data error, 
one of the numbers in the set got duplicated to another number in the set, 
which results in repetition of one number and loss of another number.
Given an array nums representing the data status of this set after the error. 
Your task is to firstly find the number occurs twice 
and then find the number that is missing. Return them in the form of an array.

eg.
Input: nums = [1,2,2,4]
Output: [2,3]
"""
class Solution(object):
    #my solution. try to use hashmap to implement
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        if nums[0] != 1:
            missing = 1
        else:
            missing = -1
        
        repeat = -1
        for i in range(len(nums)-1):
            if nums[i+1] == nums[i]:
                repeat = nums[i]
            if nums[i+1] == nums[i]+2:
                missing = (nums[i+1] + nums[i])/2
        
        if missing == -1:
            missing = nums[len(nums)-1] + 1
        return [repeat, missing]