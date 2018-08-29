"""
Given an integer, write a function to determine if it is a power of two.
"""

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # if a number, n,  is power of 2, 
        # the highest digit of binary representation is 1, the rest are zeros
        # for n-1, the highest digit is 0, the rest are ones. 
        # so bit and between n and n-1 is 0
        if n < 1:
            return False
        return n & (n - 1) == 0
