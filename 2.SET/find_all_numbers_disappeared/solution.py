class Solution(object):
    """
    Method 1 (requires extra space, a set)
    """
    def findDisappearedNumbersA(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        
        s = set(nums)
        m = len(nums)
        res = []
        temp = [ele for ele in range(1, m+1)]
        for ele in temp:
            if ele not in s:
                res.append(ele)
        return res
    
    
    """
    Method 2:
    get abs value and find its according position; negate the ele value according. 
    the positions still with positive values are missing elements. 
    """
    def findDisappearedNumbersB(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """ 
        res = []
        for i in range(len(nums)):
            index = abs(nums[i]) -1 
            nums[index] = -abs(nums[index])
        
        for j in range(len(nums)):
            if nums[j] > 0:
                res.append(j+1)
        return res
            
                    
    
  #test 
s = Solution()
nums = [4, 1, 3, 3, 2, 2, 7]
resA = s.findDisappearedNumbersA(nums)
resB = s.findDisappearedNumbersB(nums)
print(resA, resB)
