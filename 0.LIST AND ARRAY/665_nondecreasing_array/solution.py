class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        one, two = nums[:], nums[:]
        
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                one[i] = one[i+1]
                two[i+1] = two[i]
                # if we found the first pair that is out of order, we break from there.
                break
        return sorted(one) == one or sorted(two) == two

s = Solution()
nums = [8, 9, 6 , 4]
res = s.checkPossibility(nums)
print(res)