class Solution(object):

    """
    hash map
    """
    def firstMissingPositive1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = {}
        for num in nums:
            if num > 0 and num not in m:
                m[num] = num
        print(m)


        for i in range(1, len(m)+1):
            if i not in m:
                return i
        
        return len(m) + 1
    

    """
        sorting 
    """
    def firstMissingPositive2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        res = 1
        for num in nums:
            if num == res:
                res +=1 
        return res


s = Solution()

res = s.firstMissingPositive1([2])
res2 = s.firstMissingPositive2([1, 2, 4, 7,8,9,11,12])

print(res, res2)