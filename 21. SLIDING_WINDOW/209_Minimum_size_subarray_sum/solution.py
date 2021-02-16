class Solution:
    def minSubArrayLen_ver1(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        mLen = len(nums) + 1
        mSum = 0
        left, right = 0, 1
        
        for right in range(1, len(nums)+1):
            mSum = max(mSum, sum(nums[left:right]))
            if sum(nums[left:right]) >= target:
                while sum(nums[left:right]) >= target and left <= right:
                    left += 1
                mLen = min(mLen, right-left+1)
                #print(left, right, nums[left:right])
            #else:
            #   only increment right
        if mSum < target: return 0
        else: return mLen


    def minSubArrayLen_ver2(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        #rolling sum and substraction is better choice
        mLen = len(nums) + 1
        mSum, curSum = 0, 0
        left, right = 0, 1
        
        for right in range(1, len(nums)+1):
            curSum += nums[right-1]
            mSum = max(mSum, curSum)
            if curSum >= target:
                while curSum >= target and left <= right:
                    curSum -= nums[left]
                    left += 1
                mLen = min(mLen, right-left+1)

        if mSum < target: return 0
        else: return mLen