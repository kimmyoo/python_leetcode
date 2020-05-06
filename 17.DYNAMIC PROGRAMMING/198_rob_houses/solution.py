class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        #needs len(nums) spots to hold '-1'
        memo = [-1] * len(nums)
        
        def helper(nums, n):
            #base case: rob 0 house, value is 0
            if n < 0: return 0
            if memo[n] >= 0:
                return memo[n]
            memo[n] = max(helper(nums, n-2) + nums[n], helper(nums, n-1))
            return memo[n]
        
        helper(nums, len(nums)-1)
        print(memo)
        return memo[len(nums)-1]