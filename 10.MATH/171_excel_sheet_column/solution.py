import string 
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {v: index+1 for index, v in enumerate(string.ascii_uppercase)}
        sum = 0
        def value(letter, nth):
            print(nth, letter)
            return d[letter] * 26**nth
        n = len(s)
        for i in range(len(s)):
            sum += value(s[i], len(s)-i-1)
        return sum
        
#test code
s = Solution()
res1 = s.titleToNumber('AB')
res2 = s.titleToNumber('ABCD')
print(res1, res2)
