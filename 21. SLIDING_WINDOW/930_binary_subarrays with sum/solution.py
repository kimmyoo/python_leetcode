class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """

        # this solution exceeds time limit for extreme test case
        # all 0s and goal is 0.
        res, sum = 0, 0
        left = 0
        n = len(nums)

        # 
        for right in range(n):
            sum += nums[right]
            while left < right and sum > goal:
                sum -= nums[left]
                left += 1
            if sum < goal:
                continue
            if sum == goal:
                res += 1
            # looping over all leading 0s.
            # andn update res at the same time. 
            j = left
            while j < right and nums[j] == 0:
                j += 1
                res += 1
        
        return res