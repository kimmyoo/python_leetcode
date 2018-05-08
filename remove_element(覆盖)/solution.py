"""
Given an array and a value, remove all instances of that value in place
and return the new length.

The order of elements can be changed. 

It doesn't matter what you leave beyond!!!!
the new length.
"""

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = len(nums)
        j = 0
        for i in range(n):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        nums = nums[0:j]
        return j

testList = [9, 12, 23, 3, 3, 3, 3, 3, 9, 9, 1, 0, 3]
s = Solution()
newLen = s.removeElement(testList, 3)
testList = testList[0:newLen]
print (testList)
