class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        credit: huahua compare with 33. Search in Rotated Sorted Array
        """
        return self.binFindMin(nums, 0, len(nums)-1)
    
    def binFindMin(self, nums, l, r):
        #learn this trick! only one or two elements or 
        if l+1 >= r: return min(nums[l], nums[r])
        # sorted
        # print(l, r)
        if nums[l] < nums[r]: return nums[l]
        # recursively find in this half
        mid = l + (r-l)/2
        return min(self.binFindMin(nums, l, mid), self.binFindMin(nums, mid, r))