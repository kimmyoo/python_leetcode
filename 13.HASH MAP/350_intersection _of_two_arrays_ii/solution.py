"""
Given two arrays, write a function to compute their intersection.
Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
"""

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        #my own solution
        d = {}
        for e in nums1:
            if e not in d:
                d[e] = 1
            else:
                d[e] +=1
        res = []
        for e in nums2:
            if e in d and d[e] >= 1:
                res.append(e)
                #need to update number of unmatched element
                d[e]-=1
        return res
    
    
s = Solution()
nums1 = [8,8,1,2,9,2,1,4]
nums2 = [-1,2,1,8,4,9,8,100,102]
res = s.intersect(nums1, nums2)
print(res)

