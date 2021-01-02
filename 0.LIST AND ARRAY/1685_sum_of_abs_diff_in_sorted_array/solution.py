class Solution(object):
    def getSumAbsoluteDifferences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #it's a math problem in essence. 
        n = len(nums)
        prefixSum, res = [0], []
        
        # learn this way to get a prefix Sum
        for i in range(n):
            prefixSum += [nums[i] + prefixSum[-1]]
        
        # the trick here is to observe and simplify 
        # res[i] to {nums[i] * i - prefixSum[i]} + {prefixSum[n]-prefixSum[i]-nums[i]*(n-i)}
        # it's math problem
        
        for i in range(n):
            res.append(nums[i] * i - prefixSum[i] + prefixSum[n] - prefixSum[i] - nums[i]*(n-i))
        
        return res