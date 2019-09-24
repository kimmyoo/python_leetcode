class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = []
        s.append(nums[0])
        for i in range(1, len(nums)):
            if s[i-1] > 0:
                s.append(nums[i]+ s[i-1])
            else:
                s.append(nums[i])
        return max(s)


s = Solution()
nums = [3,2, -3, 100]
res = s.maxSubArray(nums)
print(res)
