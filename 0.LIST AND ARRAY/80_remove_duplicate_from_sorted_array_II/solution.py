class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre = float('-inf')
        curEleCnt = 0
        replaced = 0
        
        for i in range(len(nums)):
            if nums[i] == pre:
                curEleCnt += 1
                if curEleCnt > 2:
                    nums[i] = float('inf')
                    replaced += 1
            else:
                curEleCnt = 1
                pre = nums[i]
        nums.sort()
        return len(nums) - replaced