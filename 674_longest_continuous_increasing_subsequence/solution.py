class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        maxLen = 0
        cur = 0
        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]:
                cur +=1
                if cur > maxLen:
                    maxLen = cur
            else:
                cur = 0
        return maxLen + 1

s = Solution()
nums = [1, 2, 3, 4, 5, -1, 1, 2, 3, 4, 5, 6]
res = s.findLengthOfLCIS(nums)
print(res)
