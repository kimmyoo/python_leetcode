"""
You are given an integer array nums of size n and a positive integer k.
Divide the array into one or more arrays of size 3 satisfying 
the following conditions:

Each element of nums should be in exactly one array.
The difference between any two elements in one array is 
less than or equal to k.

Return a 2D array containing all the arrays.
 If it is impossible to satisfy the conditions, 
 return an empty array. And if there are multiple answers, return any of them.
"""

# 先从小到大排序
# 3个一组 来看每一组是不是满足条件 nums[i+2] - nums[i] <=k 
# 满足就放到res中 不满足 就 中断 return []
# 早不满足早中断，早满足 早放到 res， 最后不满足的 也肯定会中断。
# 这个理解成 greedy 也可以 

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(0, len(nums)-2, 3):
            if nums[i+2]-nums[i] <= k:
                res.append(nums[i:i+3])
            else:
                return []
        return res

