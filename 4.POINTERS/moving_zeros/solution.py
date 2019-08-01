class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        lastZero = 0
        for i in range (len(nums)):
            if nums[i] != 0:
                nums[i], nums[lastZero] = nums[lastZero], nums[i]
                lastZero+=1
            #else:
            #    do nothing but increasing i (skip all 0s and locate the first nonzero ele)
# test code 
s = Solution()
nums = [0, 0, 1, 0]
s.moveZeroes(nums)
print (nums)
