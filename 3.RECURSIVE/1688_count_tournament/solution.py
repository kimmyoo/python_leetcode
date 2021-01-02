class Solution(object):
    def __init__(self):
        self.total = 0
    
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        #base cases 1 or 2 teams
        if n == 1:
            return 0
        if n == 2:
            self.total+=1
            return self.total
   
        if n % 2 == 0:
            self.total += n//2
            self.numberOfMatches(n//2)
        else:
            self.total = (n-1)//2 + self.total
            self.numberOfMatches((n-1)//2 + 1)
        return self.total

    def numberOfMatches1(self, n):
        """
        :type n: int
        :rtype: int
        """

        res = 0
        while n > 1:
            res += n//2
            if n % 2 == 0:
                n = n//2
            else:
                n = (n-1)//2 + 1
        return res


s = Solution()
res = s.numberOfMatches(14)
res2 = s.numberOfMatches1(14)
print(res, res2)