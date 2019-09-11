class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        numString = str(x)
        for i in range(len(numString)/2):
            if numString[i] != numString[len(numString)-1 - i]:
                return False
        return True
            
s = Solution()
res1 = s.isPalindrome(-121)
res2 = s.isPalindrome(121)
print(res1, res2)