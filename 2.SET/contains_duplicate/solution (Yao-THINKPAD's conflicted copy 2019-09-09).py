"""
Given an array of integers, find if the array contains any duplicates. Your
function should return true if any value appears at least twice in the array,
and it should return false if every element is distinct.
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = set()
        for i in nums:
            if i in d:
                return True
            else:
                d.add(i)
        return False

#test is important and it goes here
test_array_a = [5, 10, 2018, 22, 33, 3]
test_array_b = [3, 2, 1, 1]

s = Solution()
res1 = s.containsDuplicate(test_array_a)
res2 = s.containsDuplicate(test_array_b)
print (res1, res2)
