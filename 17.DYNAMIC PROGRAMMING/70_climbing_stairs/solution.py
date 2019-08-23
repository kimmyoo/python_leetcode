"""
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?
Note: Given n will be a positive integer.

compare this with Fibonacci number question
"""
import numpy as np

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        stepsToN = np.zeros(n+1)
        #stepsToN is a list that represents 
        #how many ways to get to ith step
        #steps[0] is 1 because not moving is the only way
        #steps[1] is 1 because you only take 1 step to 1st step
        stepsToN[0], stepsToN[1] = 1, 1

        #the distinct ways to get to ith step is the sum of
        #stepsToN[i-1] and stepsToN[i-2]
        for i in range(2, n+1):
            stepsToN[i] = stepsToN[i-1] + stepsToN[i-2]
        return int(stepsToN[n])
    
    def climbStairs2(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        a, b= 1, 1
        for i in range(2, n+1):
            steps = a+b
            a = b
            b = steps
        return steps
        