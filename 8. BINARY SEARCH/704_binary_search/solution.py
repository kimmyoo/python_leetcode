class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = len(nums)
        left, right = 0, l-1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                left = mid+1
            else:
                right = mid-1
        return -1

s = Solution()
nums = [-100, -1, 0, 10, 1000, 12345]
target1 =  1000
target2 =  12
res1 = s.search(nums, target1)
res2 = s.search(nums, target2)
print(res1, res2)
