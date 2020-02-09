class Solution(object):
    def dominantIndex1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        sortedNums = sorted(nums)
        if sortedNums[-1] >= sortedNums[-2] * 2:
            return nums.index(sortedNums[-1])
        else:
            return -1
    
    def dominantIndex2(self, nums):
        if len(nums) == 1:
            return 0
        largest = max(nums)
        
        if all(largest >= 2 * ele for ele in nums if ele != largest):
            return nums.index(largest)
        else:
            return -1
