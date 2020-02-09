"""
Given an array consisting of n integers, 
find the contiguous subarray of given length k that has the maximum average value. 
And you need to output the maximum average value.

Example 1:
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
"""


class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        s = sum (nums[:k])
        maxSum = s
        # sum() will exceed time limit
        for i in range(1, len(nums) - k + 1 ):
            s -= nums[i-1]
            s += nums[i+k-1]
            #if s > maxSum:
            #   maxSum = s    is considered less efficient than max()
            maxSum = max(s, maxSum)
        return float(maxSum)/k


s = Solution()
nums = [1,12,-5,-6,50,3]
k = 4
res = s.findMaxAverage(nums, k)
print(res)