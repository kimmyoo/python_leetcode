"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        pos = True
        if x < 0:
            pos = False
            x = -x
        
        t = 0
        while x != 0:
            t = t * 10 + x % 10
            x //= 10     # / floating point division vs floor division
        
        if not pos:
            return -t
        return t

s = Solution()
res = s.reverse(-345)
print (res)
