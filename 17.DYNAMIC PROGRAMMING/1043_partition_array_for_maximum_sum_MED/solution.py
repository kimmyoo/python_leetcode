class Solution(object):
    def maxSumAfterPartitioning(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        credit: Huahua
        """
        n = len(A)
        dp = [0] * (n + 1)
        
        for curLen in range(1, n+1):
            #curMax will be used to find the maximum ele in the second half
            curMax = float('-inf')
            for i in range(1, min(curLen+1, K+1)):
                #every loop will update the curMax which will be used by transition function
                curMax = max(curMax, A[curLen-i])
                dp[curLen] = max(dp[curLen], dp[curLen-i] + i * curMax)
        #print(dp)
        return dp[curLen]