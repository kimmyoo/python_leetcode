class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        leftSum = 0
        rightSum = sum(nums)
        
        for i in range(len(nums)):
            leftSum += nums[i]
            if leftSum == rightSum:
                return i
            rightSum -= nums[i]
        return -1

s = Solution()
nums = [1,2,3,0,6]
res = s.pivotIndex(nums)
print(res)