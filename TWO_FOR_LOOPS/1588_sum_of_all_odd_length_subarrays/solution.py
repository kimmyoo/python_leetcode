class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        res = 0
        
        for l in range(1, n+1, 2):
            for i in range(n-l+1):
                res += sum(arr[i:i+l])
        return res