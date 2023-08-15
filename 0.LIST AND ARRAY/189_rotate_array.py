# Given an array, rotate the array to 
# the right by k steps, where k is non-negative.
# Follow up: Try to come up with an algorithm 
# that uses O(1) extra space complexity and 
# performs in linear time.

class Solution:      
    def rotate(self, nums, k):
        n = len(nums)
        k %= n
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]
        print(nums)
        nums[::] = nums[::-1]
        return nums

    def rotate2(self, nums, k):
        n = len(nums)
        k %= n

        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1
        
s = Solution()
nums = [1, 2, 3, 4, 5, 6]
k = 3
s.rotate(nums, k)
print(nums)
s.rotate2(nums, k)
print(nums)