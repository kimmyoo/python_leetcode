"""
Given an integer array, find three numbers whose product is maximum and output the maximum product.
Example 1:
Input: [1,2,3,4]
Output: 24
"""
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MIN = float('-inf')
        MAX = float('inf')
        min1, min2, max1, max2, max3 = MAX, MAX, MIN, MIN, MIN
        
        for e in nums:
            if e >= max3:
                max1 = max2
                max2 = max3
                max3 = e
            elif e >= max2:
                max1 = max2
                max2 = e
            elif e >= max1:
                max1 = e
            
            if e <= min1:
                min2 = min1
                min1 = e
            #e > min1 and e <= MAX
            elif e <= min2:
                min2 = e
        print(min1, min2, max1, max2, max3)
        return max(min1 * min2 * max3, max1 * max2 * max3)

#test
s = Solution()
nums = [1,2,3,4,-1,-100, 9]
res = s.maximumProduct(nums)
print(res)
