"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, 
called the Fibonacci sequence, such that each number is the sum of the 
two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
Given N, calculate F(N).

"""
class Solution1(object):
    def fib1(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 1 or N == 2:
            return 1
        res = self.fib1(N-1) + self.fib1(N-2)
        return res


    
    def fib_memo (self, N):
        memo = [None] * (N + 1)
        
        def fb (N, memo):
            if memo[N]:
                return memo[N]
            if N == 1 or N == 2:
                res = 1
            else:
                res = fb(N-1, memo) + fb(N-2, memo)
            memo[N] = res
            return res
        
        return fb(N, memo)


    def fib_bottom_up(self, N):
        fbSeq = [None] * (N+1)
        fbSeq[1], fbSeq[2] = 1, 1
        for i in range(3, N+1):
            fbSeq[i] = fbSeq[i-1] + fbSeq[i-2]
        
        return fbSeq[N]


s = Solution1()
resA = s.fib_memo(100) # 1000 will exceed the maximum recursion allowed.
resB = s.fib_bottom_up(1000)
print(resA, resB)