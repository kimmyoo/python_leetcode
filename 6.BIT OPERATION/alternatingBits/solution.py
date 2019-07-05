"""
Given a positive integer, check whether it has alternating bits: namely, 
if two adjacent bits will always have different values.
"""
class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        strRepr = bin(n)
        #If the iterable object is empty, the all() function also returns True
        bitCompRes = [strRepr[i] != strRepr[i+1] for i in range(len(strRepr)-1)]
        return all(bitComp)


#test code
s = Solution()
res = s.hasAlternatingBits(5)
print(res)
