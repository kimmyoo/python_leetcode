class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        dic = {}
        for num in nums:
            if num in dic:
                res += dic[num]
                dic[num] += 1
            else:
                dic[num] = 1
        return res
        # if we have seen a duplicate, we simply add dic[num] pair to res. 

s = Solution()
nums = [1,2,3,1,1,3]
ans = s.numIdenticalPairs(nums)
print(ans)