"""
Given an array of integers and an integer k, find out whether there are two
distinct indices i and j in the array such that nums[i] = nums[j] and the
difference between i and j is at most k.
"""

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # initiate a dictionary 
        # fill up the dictionary in loop with d[e] = i
        # but before doing that check whether the same element has been
        # put in the dictionary, if it's in there, check whether the newly
        # added element has difference of at least k, 
        # if yes, than return Ture
        # requires a dictionary space complexity: n
        # time complexity: n 
        d = {}
        for i, e in enumerate(nums):
            if e in d:
                #print (d[e]) # for understanding the code
                if i - d[e] <= k:
                    return True
            # only is there a duplicate, 
            # index of the most recent of occurence of e will be remembered
            # and it's totaly fine to assign different keys to the same element
            # but not the othe way around
            d[e] = i
            #print (d[e], e) # for understanding the code
        return False


args1 = [[1, 0, 1, 0, 1, 2, 2], 1]
s = Solution()
print(s.containsNearbyDuplicate(*args1))
