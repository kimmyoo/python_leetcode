"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
"""
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        l = len(nums)
        k %= l
        res = nums[len(nums)-k:]
        res.extend(nums[:len(nums)-k])
        for i in range(l):
            nums[i] = res[i]
        
s = Solution()
nums = [1,2,3,4,5,6,7]
k = 3
s.rotate(nums, k)
print(nums)