class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        memo = [[0 for i in range(n+1)] for j in range(m+1)]

        def dp(m, n, memo):
            if m < 0 or n < 0:
                return 0
            if m == 1 and n == 1:
                return 1
            print(m, n)
            if memo[m][n] > 0:
                return memo[m][n]
            topRes = dp(m, n-1, memo)
            leftRes = dp(m-1, n, memo)
            memo[m][n] = topRes + leftRes
            return memo[m][n]
        
        return dp(m, n, memo)