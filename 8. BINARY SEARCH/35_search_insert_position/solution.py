class Solution(object):
    #my solution
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def binSearch(nums, target, l, r):
            while l < r:
                mid = l + (r-l)//2
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid -1
                else:
                    return mid
            #print(l, r)
            if l > len(nums)-1:
                return l
            elif r < 0:
                return 0
            else:
                #it can also be return l if target < nums[l] else l + 1
                return r + 1 if target > nums[r] else r
        
        #edge case 
        if not nums:
            return 0
        l, r = 0, len(nums)-1
        return binSearch(nums, target, l, r)


s = Solution()
nums = [1,3,5,6]
target1, target2, target3 = 0, 4, 7
res1 = s.searchInsert(nums, target1)
res2 = s.searchInsert(nums, target2)
res3 = s.searchInsert(nums, target3)
print(res1, res2, res3)