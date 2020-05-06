"""
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?
Note: Given n will be a positive integer.
"""
class Solution(object):
    # recursive with memoization
    def climbStairsA(self, n):
        """
        :type n: int
        :rtype: int
        """
        # n + 1 sized array 
        memo = [0] * (n+1)
        memo[0], memo[1] = 1, 1
        
        for i in range(2, n+1):
            memo[i] = memo[i-1] + memo[i-2]
        return memo[n]
        
    # dp
    def climbStairsB(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 1
        
        step0, step1 = 1, 1
        #pay attention to the boundary
        for i in range(2, n+1):
            #it's easy to understand if you have middle variable called step2
            step2 = step0 + step1
            step1, step0 = step2, step1
        return step2
