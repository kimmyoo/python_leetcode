"""
Given an array of size n, find the majority element. The majority element is
the element that appears more than n/2 times.

You may assume that the array is non-empty and the majority element always
exist in the array.
"""


# easy one: use dictionary d, encounter one occurence, increment d[k]
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = len(nums) / 2
        d = {}
        for k in nums:
            if k not in d:
                d[k] = 1
            else:
                d[k] += 1
        for k in d:
            if d[k] > m:
                return k

#test code
s = Solution()
testList = [1, 1, 3, 2, 1, 3, 3, 3, 3]
res = s.majorityElement(testList)
print (res)
