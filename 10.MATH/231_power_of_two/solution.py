"""
Given an integer, write a function to determine if it is a power of two.
"""
class Solution(object):
    def isPowerOfTwoI(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n > 0 and n % 2 == 0:
            return self.isPowerOfTwo(n/2.0)
        else:
            return True if n == 1 else False
    
    #bit operation 
    def isPowerOfTwoII(self, n):
        return n > 0 and (n & n(n-1) == 0)
    
