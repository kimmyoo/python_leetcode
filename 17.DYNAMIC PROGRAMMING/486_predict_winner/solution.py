class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def minMax(nums, start, end):
            """
            :type nums: List[int]
            :type start: int
            :type end: int
            :type p1: bool
            :rtype: int
            """
            if start == end:
                return nums[start] - 0
            if memo[start][end] == float('-inf'):
                print(start, end)
                memo[start][end] = max(nums[start] - minMax(nums, start+1, end), nums[end] - minMax(nums, start, end-1))
            return memo[start][end]
        
        memo = [[float('-inf')]*len(nums) for i in range(len(nums))] 
        res = minMax(nums, 0, len(nums)-1)
        print(memo)
        return res >= 0
