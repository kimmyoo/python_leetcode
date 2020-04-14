"""
Given a collection of integers that might contain duplicates, nums, 
return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.
Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""
class Solution(object):
    def subsetsWithDup(self, nums):
        #k is the current length of subset
        #C(n, k)
        def dfs(k, start, curr):
            if len(curr) == k and curr not in res:
                res.append(curr[:])
                return
            #start is from 0 to len(nums)
            for i in range(start, n):
                # skip duplicates, if i == start, nums[i-1] will exceed array index boundary
                if i > start and nums[i] == nums[i-1]:
                    continue
                curr.append(nums[i])
                dfs(k, i + 1, curr)
                curr.pop()
        
        res = []
        n = len(nums)
        # sorting is for later to check duplicate elements
        nums.sort()
        for k in range(n + 1):
            dfs(k, first=0, curr=[])
        return res