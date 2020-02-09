class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        
        while n % 3 == 0:
            n /= 3
        
        return n == 1

    def isPowerOfTwoA(self, n):
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

    def isPowerOfTwoB(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n > 0 and n % 2 == 0:
            return self.isPowerOfTwo(n/2.0)
        else:
            return True if n == 1 else False
