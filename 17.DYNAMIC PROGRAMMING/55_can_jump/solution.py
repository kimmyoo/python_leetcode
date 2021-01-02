class Solution(object):
    #backtracking solution
    def canJumpSolA(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def canJump(idx, nums):
            if idx == len(nums)-1:
                return True
            
            furIdx = min(nums[idx] + idx, len(nums)-1)
            for nxtIdx in range(idx+1, furIdx+1):
                if canJump(nxtIdx, nums):
                    return True
            
            return False
        return canJump(0, nums)
    