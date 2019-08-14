"""
Given scores of N athletes, find their relative ranks and the people with the top three highest scores, 
who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".
"""

class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        l = len(nums)
        newNums = sorted(nums, reverse=True)
        d = {k:v for v, k in enumerate(newNums)}
        
        for k in d:
            if k == newNums[0]:
                d[k] = "Gold Medal"
            elif k == newNums[1]:
                d[k] = "Silver Medal"
            elif k == newNums[2]:
                d[k] = "Bronze Medal"
            else:
                d[k]+=1
        for i in range(l):
            nums[i] = str(d[nums[i]])
        return nums

