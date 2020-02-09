from test.test_sax import start

class Solution(object):
    def searchA(self, nums, target):
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

    #recommended by nine chapter solution
    def searchB(self, nums, target):
        l = len(nums)
        start, end = 0, l-1
        
        while start + 1 < end:
            mid = start + (end-start)/2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid
            else:
                end = mid
        
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1
         
  
s = Solution()
nums = [-100, -1, 0, 10, 1000, 12345]
target1 =  1000
target2 =  12
res1 = s.searchA(nums, target1)
res2 = s.searchB(nums, target1)
print(res1, res2)
