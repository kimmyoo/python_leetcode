class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mx = 0
        nums.sort()
        n = len(nums)
        for i in range(len(nums)/2):
            if nums[i] + nums[n-i-1] > mx:
                mx = nums[i] + nums[n-i-1]
        return mx