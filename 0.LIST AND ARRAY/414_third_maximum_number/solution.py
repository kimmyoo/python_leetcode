from collections import deque

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #remember to use set to get distint elements of the input
        #e.g. [1, 1, 2]
        if len(set(nums)) < 3:
            return max(nums)
        res = []
        for i in range(3):
            res.append(float("-inf"))
        
        for num in nums:
            res.sort()
            #remember to ignore repeating num
            if num > min(res) and num not in res:
                if len(res) > 2: res.pop(0)
                res.append(num)
        
        res.sort()
        return res[0]