"""
Given an array S of n integers, are there elements a, b, c in S such that a +
b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
"""
"""
S = -1 0 1 2 -1 -4  ==> -4, -1, -1, 0, 1, 2

"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            # i > 0 and  nums[i-1] != nums[i] is to skip duplicates elements
            # e.g.  -1, -1, 1, 0, the condition after or it to skip the second -1 in the list
            if i == 0 or (i > 0 and nums[i - 1] != nums[i]):
                left = i + 1 # set index of left end
                right = len(nums) - 1  # set the index of right end
                while left < right:
                    s = nums[i] + nums[left] + nums[right]
                    if s == 0:
                        res.append([nums[i], nums[left], nums[right]])
                        left += 1 # increment left index
                        right -= 1 # decrement right index
                        #skip all duplicate elements
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while right > left and nums[right] == nums[right + 1]:
                            right -= 1
                    elif s < 0:
                        left += 1
                    else:
                        right -= 1
        return res
