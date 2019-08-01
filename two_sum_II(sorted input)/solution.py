class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #sort array then use two pointers, one points to lower end; one points to upper end.

        lower = 0
        upper = len(nums)-1
        
        res = []
        while lower < upper:
            if nums[lower] + nums[upper] < target:
                lower+=1
            elif nums[lower] + nums[upper] > target:
                upper-=1
            else:
                res.append(lower+1)
                res.append(upper+1)
                return res


#test code
s = Solution()
nums = [1, 3, 5, 7, 9]
target = 14
res = s.twoSum(nums, target)
print (res)