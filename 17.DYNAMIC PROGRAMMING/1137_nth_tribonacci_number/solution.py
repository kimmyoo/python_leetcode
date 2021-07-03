class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        tribD = {}
        tribD[0], tribD[1], tribD[2] = 0, 1, 1
        
        def trib(n):
            if n in tribD:
                return tribD[n]
            else:
                tribD[n] = trib(n-3) + trib(n-2) + trib(n-1)
                return tribD[n]
        
        return trib(n)

s = Solution()
res = s.tribonacci(37)
print(res)