"""
Given an array of integers, return indices of the two numbers 
such that they add up to a specific target.
You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        d = {}
        for i, e in enumerate(num):
            if e in d:
                return d[e], i
            d[target - e] = i


# test 
s = Solution()
num_array = [1, 3, 5, 7, 9]
target = 4
print (s.twoSum(num_array, target))
target = 5
print (s.twoSum(num_array, target))
