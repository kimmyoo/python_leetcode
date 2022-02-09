class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        bgn, end, res  = 0, 1, []
        
        #boundary is the trick
        while end <= len(nums) - 1:
            start = bgn
            while nums[end] - nums[bgn] == 1:
                bgn += 1
                end += 1
                if end > len(nums) -1: break
           
            # need to decrement end 
            end -= 1
            if end == start:
                res.append(str(nums[start]))
                bgn += 1
                end = bgn + 1
            else:
                finish = end
                item = str(nums[start]) + "->" + str(nums[finish])
                res.append(item)
                bgn = end + 1
                end = bgn + 1
        
        # don't forget the last trailing ele
        if bgn == len(nums)-1:
            res.append(str(nums[bgn]))
        return res
                