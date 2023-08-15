
# Given a sorted array nums, 
# remove the duplicates in-place 
# such that duplicates appeared at most twice and 
# return the new length.

# Do not allocate extra space for another array;
# you must do this by modifying the input array 
# in-place with O(1) extra memory.

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre = float('-inf')
        curEleCnt = 0
        replaced = 0
        
        for i in range(len(nums)):
            if nums[i] == pre:
                curEleCnt += 1
                # at most twice
                if curEleCnt > 2:
                    nums[i] = float('inf')
                    replaced += 1
            else:
                curEleCnt = 1
                pre = nums[i]
        # print(nums)
        nums.sort()
        # print(nums)
        return len(nums) - replaced
    
    def removeDuplicates2(self, nums):
        if len(nums) <= 2:
            return len(nums)

        pos = 2

        # there is no need to check for index 0 and 1
        for i in range(2, len(nums)):
            # if the current ele is different from 
            # the element two position left
            # it means the current ele should be included in the 
            # list, so  put current  ele to pos and increment pos
            # pos indicates the insertion place
            if nums[i] != nums[pos - 2]:
                nums[pos] = nums[i]
                pos += 1
        print(nums)
        return pos
#        |i
# [1, 1, 1, 2, 3, 4, 4, 4, 5]
#        |pos

#           |i
# [1, 1, 1, 2, 3, 4, 4, 4, 5]
#        |pos

#              |i
# [1, 1, 2, 2, 3, 4, 4, 4, 5]
#           |pos


s = Solution()
l1 = [ 1, 1, 1, 2, 3, 4, 4, 4, 5]
l2 = [ 1, 1, 1, 2, 3, 4, 4, 4, 5]
res1 = s.removeDuplicates(l1)
res2 = s.removeDuplicates2(l2)
print(res1, res2)


