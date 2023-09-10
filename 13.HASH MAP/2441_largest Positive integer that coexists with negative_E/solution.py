class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        d = {}
        m = 0
        nums.sort()
        for i, num in enumerate(nums):
            if num < 0:
                if abs(num) not in d:
                    d[abs(num)] = i
            else:
                if num in d:
                    m = max(m, num)
        if m > 0:
            return m
        else:
            return -1


    # sorting by abs value
    def findMaxK2 (self, nums:list[int]) -> int:
        def customKey(x):
            absVal = -abs(x)
            sign = -1 if x < 0 else 1
            # first compare absVal( descending), then sign 
            return (absVal, sign)
        
        sortedList = sorted(nums, key=customKey)
        for i in range(1, len(sortedList)):
            if sortedList[i] == -sortedList[i-1]:
                return sortedList[i]
        return -1


s = Solution()

nums = [9, 4, 28,-3, -8, 8, -1, -23, -9, -29]
res = s.findMaxK2(nums)
print(res)