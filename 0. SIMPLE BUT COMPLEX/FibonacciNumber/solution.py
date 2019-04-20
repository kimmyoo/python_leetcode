"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, 
called the Fibonacci sequence, such that each number is the sum of the 
two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
Given N, calculate F(N).

"""

class Solution1(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 0
        if N == 1:
            return 1
        res = self.fib(N-1) + self.fib(N-2)
        return res

class Solution2(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N <= 0:
            return 0
        elif N == 1:
            return 1
        
        a, b = 0, 1
        for i in range(2, N+1):
            fn = a + b
            a = b
            b = fn
        return fn


class Solution3(object):
    def fib(self, N):
            fibs = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 
             610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 
             46368, 75025, 121393, 196418, 317811, 514229, 832040]
            return fibs[N]
